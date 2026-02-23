---
id: system
title: "3.1.1 System"
sidebar_position: 1
---


## 3.1.1. System


Each partial information display depend on CHARGER model name. 
User can read and write CHARGER system information, all item detail as below 
image and table:

![img_page10_0](/img/manual/img_page10_0.png)

Image 3-1 System information page

### System Information

|  | System Information |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Model Name | CHARGER model name | V |  |
|  | Serial Number | CHARGER serial number | V |  |
|  | System ID | Default value is model name and serial number | V | V |
|  | System Date Time | CHARGER system date & time | V | V |
|  | Ac Phase Loss Policy | The charger will check this setting to see if go into charging state under phase loss - De-rating - Stop charging | V | V |
|  | Factory Default Configuration | Request CHARGER resotre to factory default value | V | V |
|  | Authentiaction | Authorization mode - enable - disable | V | V |
|  | Authorized By EVCCID | Auto read EV MAC address as start user idtag, only effect on CCS connector. -enable -disable | V | V |
|  | Input VoltageR | AC intput vontage R phase | V |  |
|  | Input VoltageS | AC intput vontage S phase | V |  |
|  | Input VoltageT | AC intput vontage T phase | V |  |
|  | System Fan Speed | System fan speed | V |  |
|  | Rfid Card Num Endian | RFID number endianness - Little endian - Big endian | V | V |
|  | Rating Current | CHARGER rating current | V |  |
|  | Ac Rating Current | CHARGER AC rating current for third connector | V |  |
|  | APP | Using APP or not on LCM UI display | V | V |
|  | QR Code | Using QR Code or not on LCM UI display | V | V |
|  | RFID | Using RFID or not on LCM UI display | V | V |


|  | QR Code Content | QR Code Made Mode choosing “customized” | V | V |
| --- | --- | --- | --- | --- |
|  | LED Configuration Mode | LED Intensity mode - Default (100%) - Fixed Maximum (0~100%) - Sunrise/Sunsev Event(Auto) - Sunrise/Sunsev Event(Manual) | V | V |
|  | LCM Configuration Mode | LCM Intensity mode - Default (100%) - Fixed Maximum (0~100%) - Sunrise/Sunsev Event(Auto), (need internet access ability) - Sunrise/Sunsev Event(Manual), (UTC+0 timezone) | V | V |
|  | Log Include Pcap File | Log Download include CCS pcap file(DC charger only) - Exclude - Include | V | V |


![img_page13_0](/img/manual/img_page13_0.png)

### Version Information

|  | Version Information |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Csu Boot Load Fw Rev | CSU bootloader firmware version | V |  |
|  | Csu Kerne lFw Rev | CSU kernel firmware version | V |  |
|  | Csu RootFs Fw Rev | CSU RootFileSystem firmware | V |  |


|  | Csu Prim Fw Rev | Main board MCU firmware version | V |  |
| --- | --- | --- | --- | --- |
|  | Psu Prim Fw Rev | PSU primary firmware version (only display on DC model) | V |  |
|  | Psu Sec Fw Rev | PSU secondary firmware version (only display DC model) | V |  |
|  | Fan Module Fw Rev | FAN module firmware version (only display DC model) | V |  |
|  | Relay Module Fw Rev | Relay module firmware version (only display DC model) | V |  |
|  | Telcoom Modem Fw Rev | 4G module firmware version ( only display support 4G model) | V |  |
|  | Connector1 Fw Rev | Connector1 module firmware version( only display DC model) | V |  |
|  | Connector2 Fw Rev | Connector2 module firmware version( only display DC model with dual connectors) | V |  |
|  | Led Module Fw Rev | 4G module firmware version (only display DC model) | V |  |


![img_page15_0](/img/manual/img_page15_0.png)

### LCD Language Setting

|  | LCD language setting |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Default Language | LCD default display language | V | V |
|  | 2nd | Language selection item on UI | V | V |
|  | 3rd | Language selection item on UI | V | V |


| 4th | Language selection item on UI | V | V |
| --- | --- | --- | --- |
| 5th | Language selection item on UI | V | V |
| 6th | Language selection item on UI | V | V |
| 7th | Language selection item on UI | V | V |
| 8th | Language selection item on UI | V | V |
| 9th | Language selection item on UI | V | V |

Form 3-4 LCD language setting item
