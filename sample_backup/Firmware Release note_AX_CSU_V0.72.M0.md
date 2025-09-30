# Zerova AX Series – Firmware Release Notes

**CSU firmware V0.72**  
**MCU firmware B0.39**  
For: AXLU11100yxxxx-RW, AXLU19100yxxxx-RW  

**Date:** 2024-11-27

---

## Table of Contents
1. Overview  
2. CSU V0.72 Bugfixes  
3. CSU V0.72 New Features Added  
4. CSU V0.72 Design Improvements  
5. MCU B0.39 Design Improvements  
6. Firmware Release History  
7. Update Instructions  

---

## 1. Overview
This release includes significant bug fixes, new feature additions, and design improvements for the AX standard series devices (AX-32, AX-48, AX-80). The enhancements improve functionality, security, and performance. Key updates address OCPP protocol adjustments, web interface configurations, system optimizations, and added support for new standards and customer-specific customizations. :contentReference[oaicite:0]{index=0}

---

## 2. CSU V0.72 Bugfixes

### System
- **[4G]** Fix for `Module_4g`/`Module_4gSub` resource management: ensured `popen()` is matched with `pclose()` to prevent memory leaks.  
- **[WEB PAGE]** Fixed login failure when passwords contained special characters.  

### OCPP
- **OCPP 1.6:** Fixed `QrCodeContent` key name error.  
- **OCPP 1.6:** Removed extra `StopTransaction` event with PowerLoss reason during offline charging.  
- **OCPP 1.6:** Restored missing `MeterValues` for `TriggerMessage.req`.  
- **OCPP 2.0.1:** Corrected wrong or null `attributeValue`.  
- **OCPP 2.0.1:** Fixed heartbeat interval judgment logic.  
- **OCPP 2.0.1:** Corrected logic/struct type in `checkCompositeSchedule()`.  
- **OCPP 2.0.1:** Allowed variable set/get during pending `BootNotification`.  
- **OCPP 2.0.1:** Fixed `NotifyReport` message issue.  
- **OCPP 2.0.1:** Resolved crashes from hashmap mapping.  
- **OCPP 1.6 & 1.6PH:** Improved download timeout logic.  
- **OCPP 1.6/1.6PH/2.0.1:** Added `sqlite3_free_table()` to prevent memory growth.  
- **OCPP 1.6/1.6PH/2.0.1:** Fixed zip command when packing logs.  
- **OCPP 1.6/1.6PH/2.0.1:** Fixed memory leak handling `SetChargingProfileRequest`.  
- **OCPP 2.0.1:** Fixed ‘Enable’ and ‘Available’ fields mapping.  
- **OCPP 2.0.1:** Fixed `DefaultTxProfile` with `evseId=0`.  
- **OCPP 2.0.1:** Prevented continuous sending with `HeartbeatInterval=0`. :contentReference[oaicite:1]{index=1}

---

## 3. CSU V0.72 New Features Added

### System
- Added offline charging policies: **No charging (End by user)** and **No charging (End immediately)**.  
- Offline policy printing at transaction start.  
- Clear previous status data before charging.  
- IEEE 2030.5 protocol support.  
- Track charging connector insertions with reset function (MCU B0.39 required).  
- Updated default firewall whitelist: added `192.168.0.x` and `192.168.100.x`.  

### Web Page
- Added gun type “9” (NACS) for AC series.  
- Added Modbus TLS configuration and password verification.  
- Added EAP-TLS authentication configuration.  
- Added IPv6 backend client support.  
- Added VDV261 and PnC contract install/update configuration.  

### OCPP
- Added `NoActionTimeoutLimit` configuration key (OCPP 1.6).  
- Added `CentralChargeBoxId` key (OCPP 1.6PH).  
- Added `WifiMode` and `WifiToEth0Bridge`.  
- Added certificate expiration checks/renewals.  
- Enabled URLs as IPv6 addresses.  
- EVSE rejects RemoteStart for long `idTag`.  
- Added `ConnectorType`, `AvailabilityState`, and `VehicleId` variables for OCPP 2.0.1. :contentReference[oaicite:2]{index=2}

---

## 4. CSU V0.72 Design Improvements
- Lowered RootFS log auto-delete threshold to 60%.  
- Added hourly `/Storage` access mode monitoring (`check_Ubifs.sh`).  
- Verified system date on startup (&lt;2000 defaults to 2000-01-01).  
- Prevented MCU reboot output issues.  
- Optimized relay and PWM commands to send only on state change.  
- Automatic detection of power phase.  
- Synchronize `targetCurrent` to `CurrentOffer` in OCPP messages.  
- Immediate EVCCID fetch on plug-in for DIN 70121/Tesla.  
- Enhanced ISO 15118 EVCCID handling.  
- Stopped PWM before relay off (Japan JARI compliance).  
- Added two ways to check alarm/fault codes (power page button or QR code).  
- Improved QR code logic and fallback.  
- Temperature synchronization by model.  
- Enabled remote start without unplugging.  
- Converted EVCCID to lowercase for compatibility.  
- Added JARI version identification.  
- Reduced reconnect interval for IEEE 2030.5 to 10 s.  
- Synced code with CCS project V1.40.S0.  
- Optimized runtime with multithreading.  
- Updated LCM power consumption formula for CTEP 2.0.  
- Reset Modbus registers on disconnection; increased Modbus connections to 2.  
- Fixed 4G ICCID sorting, gateway check interval, and auto-restart logic.  
- Adjusted power sharing current config and encryption options.  
- Added TLS for local load balancing communication and ECDSA key uploads.  
- Numerous OCPP logic refinements for certificate handling, queueing, heartbeat, reservation, etc. :contentReference[oaicite:3]{index=3}

---

## 5. MCU B0.39 Design Improvements
- Added command to reset connector plug-in count.  
- Optimized Flash read/write process to reduce data loss risk. :contentReference[oaicite:4]{index=4}

---

## 6. Firmware Release History

| CSU Firmware | Version | Date      |
|---------------|---------|----------|
| B0.57         | Q4 2021 |
| B0.59         | Q1 2022 |
| B0.60         | Q1 2022 |
| B0.61         | Q2 2022 |
| B0.62         | Q3 2022 |
| V0.63         | Q4 2022 |
| V0.64         | Q1 2023 |
| V0.65         | Q3 2023 |
| V0.66         | Q1 2024 |
| V0.72         | Q4 2024 |

| MCU Firmware | Version | Date      |
|---------------|---------|----------|
| B0.31         | Q4 2021 |
| B0.32         | Q1 2022 |
| B0.33         | Q4 2022 |
| B0.34         | Q1 2023 |
| B0.35         | Q1 2023 |
| B0.36         | Q3 2023 |
| B0.37         | Q1 2024 |
| B0.38         | Q4 2024 |
| B0.39         | Q4 2024 |

---

## 7. Update Instructions
**Cloud Update:** Refer to section 5.19 of OCPP 1.6J for cloud-based firmware updates.  
**Local Update:** Upload the firmware image via the local update page. The charger validates the image header, performs the update in IDLE mode, and reboots automatically on completion. :contentReference[oaicite:5]{index=5}
