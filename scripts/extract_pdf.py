"""
extract_pdf.py
==============
Extract text and images from CSU3 Setting Manual PDF into Docusaurus-ready
Markdown files and image assets.

Usage (from project root, venv active):
    python scripts/extract_pdf.py [--spot-check]

Options:
    --spot-check    Print first 300 chars of each section's start page then exit.
                    Run this first to verify page-index alignment before full extraction.

Output:
    site/docs/              Markdown files organized by chapter/section
    site/static/img/manual/ Extracted PNG/JPEG images
"""

import fitz  # PyMuPDF
import re
import os
import sys
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------------------
# Paths (relative to project root)
# ---------------------------------------------------------------------------
PDF_PATH = Path("CSU3 Setting Manual_V0.23_20250930.pdf")
DOCS_OUT = Path("site/docs")
IMG_OUT  = Path("site/static/img/manual")

# ---------------------------------------------------------------------------
# Section definitions
# Pages are 0-indexed (PDF page 1 = index 0).
# ---------------------------------------------------------------------------
SECTIONS = [
    {
        "id": "connection-setup",
        "title": "Connection Setup",
        "chapter": "1",
        "pages": (6, 6),
        "file": DOCS_OUT / "01-connection-setup.md",
        "sidebar_position": 1,
        "slug": "/",
    },
    {
        "id": "access-setting-tool",
        "title": "Access to Setting Tool",
        "chapter": "2",
        "pages": (7, 7),
        "file": DOCS_OUT / "02-access-setting-tool.md",
        "sidebar_position": 2,
    },
    {
        "id": "system",
        "title": "System Settings",
        "chapter": "3.1.1",
        "pages": (9, 15),
        "file": DOCS_OUT / "settings" / "03-system.md",
        "sidebar_position": 1,
    },
    {
        "id": "charging",
        "title": "Charging Settings",
        "chapter": "3.1.2",
        "pages": (16, 21),   # page 22 has both tail of Charging + start of Network; give it to Network
        "file": DOCS_OUT / "settings" / "04-charging.md",
        "sidebar_position": 2,
    },
    {
        "id": "network",
        "title": "Network Settings",
        "chapter": "3.1.3",
        "pages": (22, 30),
        "file": DOCS_OUT / "settings" / "05-network.md",
        "sidebar_position": 3,
    },
    {
        "id": "backend",
        "title": "Backend Settings",
        "chapter": "3.1.4",
        "pages": (31, 39),
        "file": DOCS_OUT / "settings" / "06-backend.md",
        "sidebar_position": 4,
    },
    {
        "id": "upgrade",
        "title": "Upgrade",
        "chapter": "3.2",
        "pages": (40, 40),
        "file": DOCS_OUT / "settings" / "07-upgrade.md",
        "sidebar_position": 5,
    },
    {
        "id": "other",
        "title": "Other Settings",
        "chapter": "3.3",
        "pages": (41, 43),   # page 44 has both tail of Other + start of Language; give it to Language
        "file": DOCS_OUT / "settings" / "08-other.md",
        "sidebar_position": 6,
    },
    {
        "id": "language",
        "title": "Language",
        "chapter": "3.4",
        "pages": (44, 44),
        "file": DOCS_OUT / "settings" / "09-language.md",
        "sidebar_position": 7,
    },
    {
        "id": "account",
        "title": "Account",
        "chapter": "3.5",
        "pages": (45, 45),
        "file": DOCS_OUT / "settings" / "10-account.md",
        "sidebar_position": 8,
    },
    {
        "id": "modbus-server-parameters",
        "title": "Modbus Server Parameters",
        "chapter": "4.1.1",
        "pages": (46, 50),
        "file": DOCS_OUT / "appendix" / "11-modbus-server-parameters.md",
        "sidebar_position": 1,
    },
    {
        "id": "coil-table",
        "title": "Coil Table",
        "chapter": "4.1.2",
        "pages": (51, 53),
        "file": DOCS_OUT / "appendix" / "12-coil-table.md",
        "sidebar_position": 2,
    },
    {
        "id": "register-table",
        "title": "Register Table",
        "chapter": "4.1.3",
        "pages": (54, 73),
        "file": DOCS_OUT / "appendix" / "13-register-table.md",
        "sidebar_position": 3,
        "is_table": True,   # use table extraction instead of text extraction
    },
]

# ---------------------------------------------------------------------------
# Header / footer detection
# ---------------------------------------------------------------------------
def detect_recurring_lines(doc, start_page, end_page, min_occurrences=3):
    """
    Find lines that appear verbatim on min_occurrences or more pages in the
    given range. These are likely headers/footers and should be stripped.
    """
    line_counts = Counter()
    total_pages = end_page - start_page + 1
    # Cap scan at 20 pages for performance
    scan_end = min(end_page, start_page + 19)
    for i in range(start_page, scan_end + 1):
        page = doc[i]
        lines = page.get_text("text", sort=True).splitlines()
        seen_on_this_page = set()
        for line in lines:
            stripped = line.strip()
            if stripped and stripped not in seen_on_this_page:
                line_counts[stripped] += 1
                seen_on_this_page.add(stripped)
    threshold = min(min_occurrences, max(2, total_pages // 2))
    return {line for line, count in line_counts.items() if count >= threshold}


# ---------------------------------------------------------------------------
# Image extraction
# ---------------------------------------------------------------------------
def extract_images_from_page(doc, page_index, img_out_dir):
    """
    Extract all images from a page.
    Returns list of (y_top, relative_web_path) tuples so caller can do
    y-coordinate-based inline insertion.

    Fallback: if no embedded raster images exist but vector drawings cover
    more than 15% of the page area, render the drawing region to a PNG.
    """
    page = doc[page_index]
    image_list = page.get_images(full=True)
    results = []
    for img_index, img in enumerate(image_list):
        xref = img[0]
        # Get image bounding box on the page (in points)
        rects = page.get_image_rects(xref)
        y_top = rects[0].y0 if rects else 0

        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        img_filename = f"img_page{page_index + 1}_{img_index}.{ext}"
        img_path = img_out_dir / img_filename
        img_path.write_bytes(image_bytes)
        web_path = f"/img/manual/{img_filename}"
        results.append((y_top, web_path))

    return results


# ---------------------------------------------------------------------------
# Text + inline image assembly
# ---------------------------------------------------------------------------
def page_to_markdown_blocks(doc, page_index, recurring_lines, img_out_dir):
    """
    Extract text blocks from a page, strip recurring header/footer lines,
    detect and extract any tables as Markdown, and interleave image tags —
    all sorted by y-coordinate.

    Returns a list of markdown strings (text paragraphs, table strings, image
    tags) in top-to-bottom order.
    """
    page = doc[page_index]

    # --- tables: detect via find_tables(), extract as Markdown ---
    # Filter out outer "phantom" tables whose bbox fully contains another table's
    # bbox — these are false positives caused by page-level border lines.
    raw_tabs = list(page.find_tables())
    raw_rects = [fitz.Rect(t.bbox) for t in raw_tabs]

    def rect_contains(outer, inner):
        return (outer.x0 <= inner.x0 and outer.y0 <= inner.y0
                and outer.x1 >= inner.x1 and outer.y1 >= inner.y1)

    table_entries = []  # list of {"y0": float, "md": str, "rect": fitz.Rect}
    for i, tab in enumerate(raw_tabs):
        # Skip if any other table is fully inside this one (i.e., this is the outer phantom)
        if any(i != j and rect_contains(raw_rects[i], raw_rects[j])
               for j in range(len(raw_tabs))):
            continue
        extracted = tab.extract()
        if not extracted:
            continue
        # Drop a leading junk row: page-border detection sometimes captures all
        # surrounding text into the first row as one huge cell (>200 chars).
        if any(cell and len(str(cell).strip()) > 200 for cell in extracted[0]):
            extracted = extracted[1:]
        if not extracted:
            continue
        md = _rows_to_md_table(extracted)
        if md:
            table_entries.append({
                "y0": tab.bbox[1],
                "md": md,
                "rect": fitz.Rect(tab.bbox),
            })
    table_rects = [t["rect"] for t in table_entries]

    # --- text blocks (skip regions covered by a table) ---
    blocks = page.get_text("blocks", sort=True)
    # blocks: list of (x0, y0, x1, y1, text, block_no, block_type)
    # block_type 0 = text, 1 = image (handled separately)
    text_entries = []
    for b in blocks:
        if b[6] != 0:   # skip non-text blocks
            continue
        x0, y0, x1, y1, raw = b[0], b[1], b[2], b[3], b[4]
        br = fitz.Rect(x0, y0, x1, y1)
        if any(br.intersects(tr) for tr in table_rects):
            continue    # this text belongs to a table cell — skip it
        lines = raw.splitlines()
        clean = [l for l in lines if l.strip() not in recurring_lines]
        text = "\n".join(clean).strip()
        if text:
            text_entries.append({"y0": y0, "text": text})

    # --- images with y positions ---
    images = extract_images_from_page(doc, page_index, img_out_dir)

    # --- merge all content by y-coordinate ---
    all_items = []  # list of (y0, content_string)
    for te in text_entries:
        all_items.append((te["y0"], te["text"]))
    for tab in table_entries:
        all_items.append((tab["y0"], "\n" + tab["md"]))
    for y_img, web_path in images:
        alt = Path(web_path).stem
        all_items.append((y_img, f"\n![{alt}]({web_path})\n"))

    all_items.sort(key=lambda x: x[0])
    return [item[1] for item in all_items]


def text_cleanup(text):
    """Light normalisation: collapse 3+ blank lines → 2, fix broken hyphenation."""
    # Strip version header (e.g. "Version 0.24   (2025/09/30)")
    text = re.sub(r"Version\s+\d+\.\d+\s+\(\d{4}/\d{2}/\d{2}\)", "", text)
    # Strip bare document title line
    text = re.sub(r"CSU3 Setting Manual\s*", "", text)
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Re-join lines broken mid-word by hyphenation (word- \n word → wordword)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    # Fix Chinese full-width colon → ASCII colon
    text = text.replace("：", ":")
    # Normalize fragmented bullet points: "-\n  word" → "- word"
    text = re.sub(r"-\s*\n\s+(\S)", r"- \1", text)
    return text.strip()


def heading_detect(text):
    """
    Promote lines that look like section headings to Markdown headings.
    Matches patterns like "3.1.1 System" or "4.1 Modbus Information".
    """
    lines = text.split("\n")
    out = []
    for line in lines:
        stripped = line.strip()
        # Guard: skip "N of M" page-number patterns (e.g. "7 of 74")
        if re.match(r"^\d+\s+of\s+\d+$", stripped):
            continue
        if re.match(r"^\d+(\.\d+){0,3}\.?\s+\S.{0,60}$", stripped) and len(stripped) < 80:
            out.append(f"\n## {stripped}\n")
        else:
            out.append(line)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Table extraction (Modbus register table)
# ---------------------------------------------------------------------------
def extract_table_as_markdown(doc, start_page, end_page):
    """
    Primary: PyMuPDF find_tables() — works when table borders are vector lines.
    Fallback: word-clustering by x-coordinate column bands.
    Returns a Markdown table string.
    """
    # --- Primary: find_tables ---
    all_rows = []
    for page_idx in range(start_page, end_page + 1):
        page = doc[page_idx]
        tabs = page.find_tables()
        for tab in tabs:
            extracted = tab.extract()
            if extracted:
                all_rows.extend(extracted)

    if all_rows:
        return _rows_to_md_table(all_rows)

    # --- Fallback: word clustering ---
    print("  [warn] find_tables() returned nothing — using word-clustering fallback")
    return _word_cluster_table(doc, start_page, end_page)


def _rows_to_md_table(rows):
    """Convert list-of-lists rows into a Markdown table string."""
    if not rows:
        return ""
    # Normalise None cells
    rows = [[cell if cell is not None else "" for cell in row] for row in rows]
    # Determine max column count
    ncols = max(len(r) for r in rows)
    # Pad all rows to ncols
    rows = [(r + [""] * ncols)[:ncols] for r in rows]

    def escape(cell):
        return cell.replace("|", "\\|").replace("\n", " ").strip()

    header = rows[0]
    md = "| " + " | ".join(escape(c) for c in header) + " |\n"
    md += "| " + " | ".join(["---"] * ncols) + " |\n"
    for row in rows[1:]:
        md += "| " + " | ".join(escape(c) for c in row) + " |\n"
    return md


def _word_cluster_table(doc, start_page, end_page):
    """
    Fallback table extractor using word bounding boxes.
    Groups words into columns by x-coordinate proximity, then into rows by y.
    Returns Markdown table string.
    """
    all_words = []
    for page_idx in range(start_page, end_page + 1):
        page = doc[page_idx]
        words = page.get_text("words", sort=True)
        # words: (x0, y0, x1, y1, word, block_no, line_no, word_no)
        for w in words:
            all_words.append({"x0": w[0], "y0": w[1], "x1": w[2], "y1": w[3], "text": w[4]})

    if not all_words:
        return "_No table data extracted._\n"

    # Cluster x-midpoints into columns (gap-based)
    x_mids = sorted(set(round((w["x0"] + w["x1"]) / 2) for w in all_words))
    col_boundaries = []
    prev = x_mids[0]
    group_start = prev
    for x in x_mids[1:]:
        if x - prev > 20:   # gap > 20pt signals a new column
            col_boundaries.append((group_start, prev))
            group_start = x
        prev = x
    col_boundaries.append((group_start, prev))

    def assign_col(word):
        mid = (word["x0"] + word["x1"]) / 2
        for i, (lo, hi) in enumerate(col_boundaries):
            if lo - 15 <= mid <= hi + 15:
                return i
        return len(col_boundaries)  # overflow column

    # Group words by row (y0 proximity within 5pt)
    y_positions = sorted(set(round(w["y0"]) for w in all_words))
    row_ys = []
    if y_positions:
        row_start = y_positions[0]
        prev_y = y_positions[0]
        for y in y_positions[1:]:
            if y - prev_y > 5:
                row_ys.append(row_start)
                row_start = y
            prev_y = y
        row_ys.append(row_start)

    # Build row → col → text mapping
    row_data = {ry: [""] * (len(col_boundaries) + 1) for ry in row_ys}
    for w in all_words:
        ry = min(row_ys, key=lambda y: abs(y - w["y0"]))
        col = assign_col(w)
        if col < len(row_data[ry]):
            row_data[ry][col] += (" " if row_data[ry][col] else "") + w["text"]

    rows = [row_data[ry] for ry in sorted(row_data.keys())]
    return _rows_to_md_table(rows)


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------
def build_frontmatter(section):
    fm = (
        "---\n"
        f"id: {section['id']}\n"
        f"title: \"{section['title']}\"\n"
        f"sidebar_position: {section['sidebar_position']}\n"
    )
    if "slug" in section:
        fm += f"slug: {section['slug']}\n"
    fm += "---\n\n"
    return fm


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def spot_check(doc):
    """Print first 300 chars of each section's start page for verification."""
    print("\n=== SPOT CHECK — first 300 chars of each section start page ===\n")
    for sec in SECTIONS:
        start = sec["pages"][0]
        page = doc[start]
        text = page.get_text("text", sort=True)[:300].replace("\n", " ")
        print(f"[{sec['chapter']}] {sec['title']} (page index {start}):")
        safe = text.encode("ascii", errors="replace").decode("ascii")
        print(f"  {safe!r}")
        print()
    print("=== Review the above, then re-run without --spot-check ===")


def main():
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at {PDF_PATH.resolve()}")
        sys.exit(1)

    doc = fitz.open(PDF_PATH)
    print(f"Opened: {PDF_PATH} ({len(doc)} pages)")

    if "--spot-check" in sys.argv:
        spot_check(doc)
        doc.close()
        return

    # Create output directories
    for path in [DOCS_OUT, IMG_OUT,
                 DOCS_OUT / "settings", DOCS_OUT / "appendix"]:
        path.mkdir(parents=True, exist_ok=True)

    # Detect recurring header/footer lines across the full document
    print("Detecting recurring header/footer lines…")
    recurring = detect_recurring_lines(doc, 0, len(doc) - 1)
    if recurring:
        print(f"  Will strip {len(recurring)} recurring line(s): "
              + ", ".join(repr(r) for r in list(recurring)[:5])
              + ("..." if len(recurring) > 5 else ""))
    else:
        print("  None detected.")

    # Process each section
    for sec in SECTIONS:
        start, end = sec["pages"]
        out_file = Path(sec["file"])
        out_file.parent.mkdir(parents=True, exist_ok=True)

        fm = build_frontmatter(sec)

        if sec.get("is_table"):
            # Dedicated table extraction for register/coil tables
            print(f"  Extracting table: {sec['title']} (pages {start+1}–{end+1})")
            table_md = extract_table_as_markdown(doc, start, end)
            content = fm + f"# {sec['chapter']} {sec['title']}\n\n" + table_md
        else:
            # Text + image extraction
            print(f"  Extracting: {sec['title']} (pages {start+1}–{end+1})")
            page_blocks = []
            for page_idx in range(start, end + 1):
                blocks = page_to_markdown_blocks(doc, page_idx, recurring, IMG_OUT)
                page_blocks.extend(blocks)

            body = "\n\n".join(b for b in page_blocks if b.strip())
            body = text_cleanup(body)
            body = heading_detect(body)
            content = fm + body

        out_file.write_text(content, encoding="utf-8")
        print(f"    -> {out_file}")

    doc.close()
    print("\nExtraction complete.")
    print(f"  Docs:   {DOCS_OUT.resolve()}")
    print(f"  Images: {IMG_OUT.resolve()}")


if __name__ == "__main__":
    main()
