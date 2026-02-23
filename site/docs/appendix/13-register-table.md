---
id: register-table
title: "4.1.3 Register Table"
sidebar_position: 3
---

# 4.1.3 Register Table

|  | Register usage |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Description |  | EVSE AC Input voltage R (kW). |  |  |  |
| Register address |  | 96 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.5. Present input Voltage L2 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | EVSE AC input voltage S (kW). |  |  |  |
| Register address |  | 98 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.6. Present input Voltage L3 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | EVSE AC input voltage T (kW). |  |  |  |
| Register address |  | 100 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.7. Present input Voltage DC |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | EVSE DC input voltage (kW). |  |  |  |
| Register address |  | 102 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE perform to authorize Idtag before start charging session. |  |  |  |
| Register address |  | 564 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | 0 | Disable |  |  |
|  |  | 1 | Enable |  |  |
| 4.1.3.9. Authentication by EVCCID |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE perform to get EVCCID from EV as Idtag. |  |  |  |
| Register address |  | 565 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | 0 | Disable |  |  |
|  |  | 1 | Enable |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE each charging session maximum charged energy (kWh). |  |  |  |
| Register address |  | 566 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | 0 | Unlimit |  |  |
|  |  | 1~65535 | kWh |  |  |
| 4.1.3.11. Maximum charging power |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE each charging session maximum charging power (kW), only effect on DC model. |  |  |  |
| Register address |  | 567 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range |  | Notes |  |
|  |  | 0 |  | Unlimit |  |
|  |  | 1~Rating power |  | kW |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE each charging session maximum charging current (A). |  |  |  |
| Register address |  | 568 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range | Notes |  |  |
|  |  | 0 | Unlimit |  |  |
|  |  | 1~Rating current | A |  |  |
| 4.1.3.13. Maximum charging duration |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE each charging session maximum charged duration (Minute). |  |  |  |
| Register address |  | 569 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range | Notes |  |  |
|  |  | 0 | Unlimit |  |  |
|  |  | 1~65535 | Minutes |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE read RFID SN direction |  |  |  |
| Register address |  | 570 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range | Notes |  |  |
|  |  | 0 | Little endian |  |  |
|  |  | 1 | Big endian |  |  |
| 4.1.3.15. ISO-15118 enable |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE support ISO-15118 communication protocol |  |  |  |
| Register address |  | 571 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range | Notes |  |  |
|  |  | 0 | Disable |  |  |
|  |  | 1 | Enable |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Configure EVSE support ISO-15118 PnC mechanism |  |  |  |
| Register address |  | 572 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | R/W |  |  |  |
| Parameter |  | Range | Range |  |  |
|  |  | 0 | Disable |  |  |
|  |  | 1 | Enable |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector currently system state |  |  |  |
| Register address |  | (id*1000) + 0 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | Value | Notes |  |  |
|  |  | 0 | Booting |  |  |
|  |  | 1 | Idle |  |  |
|  |  | 2 | Authorizing |  |  |
|  |  | 5 | Preparing |  |  |
|  |  | 8 | Charging |  |  |
|  |  | 9 | Terminating |  |  |
|  |  | 10 | Complete |  |  |
|  |  | 11 | Alarm |  |  |
|  |  | 12 | Fault |  |  |
|  |  | 13 | Reservation |  |  |
|  |  | 15 | Maintain |  |  |
|  |  | 19 | Upgrade |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector and EV socket connection status |  |  |  |
| Register address |  | (id*1000) + 1 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | Value | Value |  |  |
|  |  | 0 | Disconnected |  |  |
|  |  | 1 | Connected |  |  |
| 4.1.3.19. Present charging session SOC |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session SOC (%) on EV side |  |  |  |
| Register address |  | (id*1000) + 2 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.20. Present charging output power |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output power (kW) |  |  |  |
| Register address |  | (id*1000) + 3 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output voltage (V), only effect DC connector. |  |  |  |
| Register address |  | (id*1000) + 5 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.22. Present charging output voltage AC L1 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L1 voltage (V), only effect AC connector. |  |  |  |
| Register address |  | (id*1000) + 7 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.23. Present charging output voltage AC L2 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L2 voltage (V), only effect AC connector with 3 phase power. |  |  |  |
| Register address |  | (id*1000) + 9 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L3 voltage (V), only effect AC connector with 3 phase power. |  |  |  |
| Register address |  | (id*1000) + 11 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.25. Present charging output current DC |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output current (A), only effect DC connector. |  |  |  |
| Register address |  | (id*1000) + 13 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.26. Present charging output current AC L1 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L1 current (A), only effect AC connector. |  |  |  |
| Register address |  | (id*1000) + 15 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L2 current (A), only effect AC connector with 3 phase power. |  |  |  |
| Register address |  | (id*1000) + 17 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.28. Present charging output current AC L3 |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output L3 current (A), only effect AC connector with 3 phase power. |  |  |  |
| Register address |  | (id*1000) + 19 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.29. Present charged energy |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session output energy (kWh) |  |  |  |
| Register address |  | (id*1000) + 21 |  |  |  |
| Length |  | 2 word in float |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session duration (second) |  |  |  |
| Register address |  | (id*1000) + 25 |  |  |  |
| Length |  | 2 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.31. Present charging session remain time |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session remain time (second), only effect DC connector |  |  |  |
| Register address |  | (id*1000) + 27 |  |  |  |
| Length |  | 2 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.32. Present charging session idtag |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session start user, only effect DC connector |  |  |  |
| Register address |  | (id*1000) + 29 |  |  |  |
| Length |  | 10 word in string |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.33. Connector plugged count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present plugged accumulative count |  |  |  |
| Register address |  | (id*1000) + 39 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector accumulative output energy (kWh) |  |  |  |
| Register address |  | (id*1000) + 41 |  |  |  |
| Length |  | 2 words in float |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.35. Connector status code (ASCII) |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present status code in ASCII format |  |  |  |
| Register address |  | (id*1000) + 50 |  |  |  |
| Length |  | 40 word in string |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | If there are two above status code occur mean time, code will distinguish in comma flag. |  |  |  |
| 4.1.3.36. Connector status code (Integer) |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present status code in integer format |  |  |  |
| Register address |  | (id*1000) + 90 |  |  |  |
| Length |  | 10 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | If there are two above status code occur mean time, status code will put on next register. |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present temperature in Celsius |  |  |  |
| Register address |  | (id*1000) + 100 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | This register only effect with connector support temperature detect feature |  |  |  |
| 4.1.3.38. Connector charging session EVCCID |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector present charging session EVCCID |  |  |  |
| Register address |  | (id*1000) + 101 |  |  |  |
| Length |  | 10 words in string |  |  |  |
| Permission |  | Read only |  |  |  |
| Parameter |  | This register only effect with CCS connector |  |  |  |
| 4.1.3.39. Connector ID |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Connector ID |  |  |  |
| Register address |  | (id*1000) + 111 |  |  |  |
| Length |  | 1 word in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) AC breaker usage time in second, this only for DC model |  |  |  |
| Register address |  | 20000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.41. Charger AC contactor cycle count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) AC contactor ON/OFF cycle count, this only for DC model |  |  |  |
| Register address |  | 20002 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.42. Charger AC filter usage time |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) filter usage time in second, this only for DC model |  |  |  |
| Register address |  | 20004 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) output relay quantity, one output connector will equip K1/K2 relay set, this only for DC model |  |  |  |
| Register address |  | 21000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.44. Charger K1 output relay usage count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) output relay K1 usage count, this only for DC model, id start from 1 to charger output relay set quantity. |  |  |  |
| Register address |  | (id*100) + 21000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.45. Charger K2 output relay usage count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) output relay K2 usage count, this only for DC model, id start from 1to charger output relay set quantity. |  |  |  |
| Register address |  | (id*100) + 21002 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) bridge relay quantity, one bridge set will equip P/N relay set, this only for DC model |  |  |  |
| Register address |  | 24000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.47. Charger P bridge relay usage count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) P bridge relay usage count, this only for DC model, id start from 1 to charger bridge relay quantity. |  |  |  |
| Register address |  | (id*100) + 24000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.48. Charger N bridge relay usage count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Charger (DO/DB/DK/DZ model is cabinet) N bridge relay usage count, this only for DC model, id start from 1 to charger bridge relay quantity. |  |  |  |
| Register address |  | (id*100) + 24002 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser quantity on cabinet, this only for DO/DB/DK/DZ model |  |  |  |
| Register address |  | 25000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.50. Dispenser AC breaker use time |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser AC breaker usage time in second, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity. |  |  |  |
| Register address |  | (id*1000) + 25000 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.51. Dispenser AC contactor cycle count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser AC contactor ON/OFF cycle count, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity. |  |  |  |
| Register address |  | (id*1000) + 25002 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser filter usage time in second, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity. |  |  |  |
| Register address |  | (id*1000) + 25004 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.53. Dispenser output relay quantity |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser output relay quantity, one output connector will equip K1/K2 relay set, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity. |  |  |  |
| Register address |  | (id*1000) + 25500 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
| 4.1.3.54. Dispenser K1 output relay usage count |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser output relay K1 usage count, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity and sub id start from 1 to dispenser output relay _ quantity. |  |  |  |
| Register address |  | (id*100) + 25500 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
|  | Register usage |  |  |  |  |
| Description |  | Dispenser output relay K2 usage count, this only for DO/DB/DK/DZ model, id start from 1 to dispenser quantity and sub id start from 1 to dispenser output relay _ quantity. |  |  |  |
| Register address |  | (id*100) + 25502 |  |  |  |
| Length |  | 2 words in integer |  |  |  |
| Permission |  | Read only |  |  |  |
|  |  |  |  |  |  |
