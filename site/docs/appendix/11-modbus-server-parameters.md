---
id: modbus-server-parameters
title: "4.1.1 Modbus Server Parameters"
sidebar_position: 1
---


## 4. Appendix



## 4.1. Modbus information


Data endian default is little endian unless specified on each register 
description


## 4.1.1. Modbus server parameters


|  | Parameters of CSUs |  |  |
| --- | --- | --- | --- |
| Modbus port |  | 502 |  |
| Size of nb bits |  | 39000 |  |
| Size of nb input bits |  | 39000 |  |
| Size of nb registers |  | 39000 |  |
| Size of nb input registers |  | 39000 |  |

Form 4-1 Modbus TCP Server parameters

![img_page47_0](/img/manual/img_page47_0.png)

Image 4-1 Modbus access desciption



## 4.1.2. Coil table


Following is the summary table of coil, which is using coil (function code is 
0x01/0x05). Please refer start from charter 4.1.2.1 for the detail.

|  | Bit group |  |  | Address of coil |  |  | Name |  |  | Type |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Common operation bits |  |  | 0 |  |  | Write EVSE configuration value request |  |  | W |  |  |
|  |  |  | 1 |  |  | EVSE reboot request |  |  | W |  |  |
|  |  |  | 2 |  |  | String data MSB request |  |  | W |  |  |
|  |  |  | 3 |  |  | String data MSW request |  |  | W |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
| Connector-id operation bits (id start since 1) |  |  | (id*1000) + 0 |  |  | Coonector-1 start charging request |  |  | W |  |  |
|  |  |  | (id*1000) + 1 |  |  | Coonector-1 stop charging request |  |  | W |  |  |
|  |  |  | (id*1000) + 2 |  |  | Coonector-1 operative request |  |  | W |  |  |
|  |  |  | (id*1000) + 3 |  |  | Coonector-1 inoperative request |  |  | W |  |  |
|  |  |  | (id*1000) + 4 |  |  | Coonector-1 plugged count clear request |  |  | W |  |  |
|  |  |  | … |  |  | Reserve |  |  |  |  |  |
|  |  |  | (id*1000) + 999 |  |  |  |  |  |  |  |  |

Form 4-2 Modbus coil table

4.1.2.1. 
Write EVSE configuration value request

Coil usage

External control system request EVSE write currently configuration value on

Description

holding register to NAND flash.

Coil address 
0

Permission 
Write only


4.1.2.2. 
EVSE reboot request

|  | Coil usage |  |  |
| --- | --- | --- | --- |
| Description |  | External control system request EVSE perform system reboot. |  |
| Coil address |  | 1 |  |
| Permission |  | Write only |  |
| 4.1.2.3. String data byte swap request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request EVSE put string data with byte swap. |  |
| Coil address |  | 2 |  |
| Permission |  | Write only |  |
| 4.1.2.4. String data word swap request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request EVSE put string data with word swap. |  |
| Coil address |  | 3 |  |
| Permission |  | Write only |  |
| 4.1.2.5. Connector start charging request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request connector start charging session. |  |
| Coil address |  | (id*1000) |  |
| Permission |  | Write only |  |


4.1.2.6. 
Connector stop charging request

|  | Coil usage |  |  |
| --- | --- | --- | --- |
| Description |  | External control system request connector stop charging session. |  |
| Coil address |  | (id*1000)+1 |  |
| Permission |  | Write only |  |
| 4.1.2.7. Connector operative request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request connector operative. |  |
| Coil address |  | (id*1000)+2 |  |
| Permission |  | Write only |  |
| 4.1.2.8. Connector inoperative request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request connector inoperative. |  |
| Coil address |  | (id*1000)+3 |  |
| Permission |  | Write only |  |
| 4.1.2.9. Connector plugged count clear request |  |  |  |
|  | Coil usage |  |  |
| Description |  | External control system request to clear connector plugged count. |  |
| Coil address |  | (id*1000)+4 |  |
| Permission |  | Write only |  |



## 4.1.3. Register table


Following is the summary table of register, which is using holding register (function 
code is 0x03/0x06). Please refer start charter 4.1.3.1 for the detail. 
 
Data endian default is little endian unless specified on each register description

|  | Register group |  | Address of |  | Name | Type |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | holding |  |  |  |
|  |  |  | Register |  |  |  |
|  | EVSE info | 0 |  |  | Model name | R |
|  |  | 32 |  |  | Serial number | R |
|  |  | 64 |  |  | Login password | W |
|  |  | 96 |  |  | Present AC input voltage L1 | R |
|  |  | 98 |  |  | Present AC input voltage L2 | R |
|  |  | 100 |  |  | Present AC input voltage L3 | R |
|  |  | 102 |  |  | Present DC input voltage | R |
|  | EVSE configuration | 564 |  |  | Authentication enable | R/W |
|  |  | 565 |  |  | Authentication by EVCCID | R/W |
|  |  | 566 |  |  | Maximum charging energy (kWh) | R/W |
|  |  | 567 |  |  | Maximum charging power (kW) | R/W |
|  |  | 568 |  |  | Maximum charging current (A) | R/W |
|  |  | 569 |  |  | Maximum charging duration (Minutes) | R/W |
|  |  | 570 |  |  | RFID endian | R/W |
|  |  | 571 |  |  | ISO-15118 enable | R/W |
|  |  | 572 |  |  | ISO-15118 PnC enable | R/W |
|  | Connector-id info (id start from 1) | (id*1000) + 0 |  |  | Connector system status | R |
|  |  | (id*1000) + 1 |  |  | Connector plug status | R |
|  |  | (id*1000) + 2 |  |  | Present charging session SOC (%) | R |
|  |  | (id*1000) + 3 |  |  | Present charging output power (kW) | R |
|  |  | (id*1000) + 5 |  |  | Present charging output voltage DC (V) | R |
|  |  | (id*1000) + 7 |  |  | Present output voltage AC L1 (V) | R |
|  |  | (id*1000) + 9 |  |  | Present output voltage AC L2 (V) | R |
|  |  | (id*1000) + 11 |  |  | Present output voltage AC L3 (V) | R |
|  |  | (id*1000) + 13 |  |  | Present output current DC (A) | R |
|  |  | (id*1000) + 15 |  |  | Present output current AC L1 (A) | R |
|  |  | (id*1000) + 17 |  |  | Present output current AC L2 (A) | R |
|  |  | (id*1000) + 19 |  |  | Present output current AC L3 (A) | R |
