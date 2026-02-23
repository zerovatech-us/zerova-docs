---
id: coil-table
title: "4.1.2 Coil Table"
sidebar_position: 2
---

|  |  | (id*1000) + 21 | Present charged energy (kWh) | R |
| --- | --- | --- | --- | --- |
|  |  | (id*1000) + 25 | Present charged duration (Second) | R |
|  |  | (id*1000) + 27 | Present charging session remain time (Second) | R |
|  |  | (id*1000) + 29 | Present charging session idtag | R |
|  |  | (id*1000) + 39 | Connector plugged count | R |
|  |  | (id*1000) + 41 | Connector Accumulate output energy (KWH) | R |
|  |  | (id*1000) + 50 | Connector status code in ASCII format | R |
|  |  | (id*1000) + 90 | Connector status code in integer format | R |
|  |  | (id*1000) + 100 | Connector temperature | R |
|  |  | (id*1000) + 101 | Connector charging session EVCCID | R |
|  |  | (id*1000) + 111 | Connector ID | R |
|  | Key parts information (id / sub id _ start from 1) | 20000 | Charger(cabinet) AC breaker usage time | R |
|  |  | 20002 | Charger(cabinet) AC contactor cycle count | R |
|  |  | 20004 | Charger(cabinet) filter usage time | R |
|  |  | 21000 | Charger(cabinet) output relay quantity (id) | R |
|  |  | (id*100) + 21000 | K1 output relay usage count | R |
|  |  | (id*100) + 21002 | K2 output relay usage count | R |
|  |  | 24000 | Charger(cabinet) bridge relay quantity (id) | R |
|  |  | (id*100) + 24000 | P bridge relay usage count | R |
|  |  | (id*100) + 24002 | N bridge relay usage count | R |
|  |  | 25000 | Dispenser quantity (id) | R |
|  |  | (id*1000) + 25000 | Dispenser AC breaker usage time | R |
|  |  | (id*1000) + 25002 | Dispenser AC contactor cycle count | R |
|  |  | (id*1000) + | Dispenser filter usage time | R |


|  | 25004 |  |  |
| --- | --- | --- | --- |
|  | (id*1000) + 25500 | Dispenser output relay quantity (sub id) _ | R |
|  | (id*1000) + (sub id*100) + _ 25500 | Dispenser K1 output relay usage count | R |
|  | (id*1000) + (sub id*100) + _ 25502 | Dispenser K2 output relay usage count | R |

Form 4-3 Modbus register table

Hierarchy

Component Name
Register address
AC breaker
20000
AC contactor
20002
filter 
20004
Output relay set quantity
21000
Connector-1 K1 relay
(id*100)+21000
Connector-1 K2 relay
(id*100)+21002
…
(id*100)+21000
…
(id*100)+21002
Bridge relay set quantity
24000
Bridge-1 P relay
(id*100)+24000
Bridge-1 N relay
(id*100)+24002
…
(id*100)+24000
…
(id*100)+24002
Dispenser quantity
25000
AC breaker
(id*1000)+25000
AC contactor
(id*1000)+25002
filter 
(id*1000)+25004
Output relay set quantity
(id*1000)+25500
Connector-1 K1 relay
(id*1000)+(sub_id*100)+25500
Connector-1 K2 relay
(id*1000)+(sub_id*100)+25502
…
(id*1000)+(sub_id*100)+25500
…
(id*1000)+(sub_id*100)+25502

Output relay
(id start from 1 to output relay set

quantity)

Bridge relay
(id start from 1 to Bridge relay

Charger (Cabine

quantity)

Dispenser
(id start from 1 to

dispenser

Output relay
(sub_id start from

quantity)


## 1 to output relay


Form 4-4 Key parts modbus register archietecture table

set quantity)


4.1.3.1. 
Model name

|  |  |  |  |
| --- | --- | --- | --- |
|  | Register usage |  |  |
| Description |  | EVSE model name information |  |
| Register address |  | 0 |  |
| Length |  | 32 word in string |  |
| Permission |  | Read only |  |
| 4.1.3.2. Serial number |  |  |  |
|  | Register usage |  |  |
| Description |  | EVSE serial number information |  |
| Register address |  | 32 |  |
| Length |  | 32 word in string |  |
| Permission |  | Read only |  |
| 4.1.3.3. Login password |  |  |  |
|  | Register usage |  |  |
| Description |  | Login password before access modbus info must write correct password. |  |
| Register address |  | 64 |  |
| Length |  | 32 word in string |  |
| Permission |  | W |  |
| Parameter |  | This content is password sha256 hash result in lower case |  |
