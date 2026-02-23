---
id: backend
title: "3.1.4 Backend"
sidebar_position: 4
---


## 3.1.4. Backend


![img_page32_0](/img/manual/img_page32_0.png)

Image 3-12 Backend common information page

### Common

| Common Information |  |  |  |
| --- | --- | --- | --- |
| Field Name | Description | Attributes |  |
|  |  | Read | Write |
| Backend Connection Timeout | Timeout limit of connecting to backend | V | V |


|  | Offline Policy | CHARGER offline charging policy - Local list - Free charging - No charging (End by user) - No charging (End immediately) | V | V |
| --- | --- | --- | --- | --- |
|  | Offline Max Charge Energy | CHARGER offline charging energy 0:MaxChargingEnergy 1~65535 KWH | V | V |
|  | Offline Max Charge Duration | CHARGER offline charging duration 0:MaxChargeDuration 1~65535 Minutes | V | V |
|  | Offline Max Charge Power | CHARGER offline mximum output power，only DC model 0: MaxChargePower 1~65535 kWh | V | V |
|  | Offline Max Charge Current | CHARGER offline mximum output current，only AC model 0: MaxChargePower 1~65535 amp | V | V |


![img_page34_0](/img/manual/img_page34_0.png)

Image 3-13 Ocpp backend information page

### OCPP Backend

|  | OCPP Backend |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Ocpp Connection Status | The connection status of OCPP backend | V |  |
|  | Central System URL | The OCPP server url which include port which charger want to connected. ws: non-secure OCPP 1.6-J wss: secure OCPP 1.6-J Ex: ws://ocpp.phihong.com.tw:80/ wss://ocpp.phihong.com.tw:443/ | V | V |
|  | Charge BoxId | The charge box ID will use to connect to OCPP server | V | V |
|  | Charge Point Vendor | Charger vender name | V | V |
|  | Ocpp Security Profile | Ocpp Security Profile - None security - Unsecured Transport with Basic Atuentication - TLS with Basic Authentication - TLS with Client Side Certificates | V | V |
|  | Ocpp Security Password | Displayed when “Ocpp Security Profile” is 「Unsecured Transport with Basic Atuentication」 or「TLS with Basic Authentication」 | V | V |
|  | Receipt URL | Receipt QR code URL content, if filled out value when charging session end LCM will display QR Code for end user scan to get receipt info. | V | V |
|  | Maintain Server Connection Status | The connection status of maintain backend | V |  |
|  | Maintain Server URL | The maintain server url which include port which charger want | V | V |


|  | Maintain Server Security Profile | Ocpp Security Profile - None security - Unsecured Transport with Basic Atuentication - TLS with Basic Authentication | V | V |
| --- | --- | --- | --- | --- |


![img_page37_0](/img/manual/img_page37_0.jpeg)

### Local Load Balance

|  | Local loading balance |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Local Loading Balance | Local Loading Balance - Disable - Client Server | V | V |
|  | Power Sharing Capacity | Power capacity when local loading balance configure as server. | V | V |
|  | Power Sharing Server IP | Target server IP when local loading balance configure as client | V | V |

Form 3-15 Local loading balance information item


![img_page38_0](/img/manual/img_page38_0.png)

### TTIA Backend

|  | TTIA Backend(for CNS only) |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | TTIA | TTIA setting enable or disable | V | V |
|  | Server Address | The TTIA server url which charger want to connected. | V | V |
|  | Server Port | The TTIA server port which charger want to connected. | V | V |
|  | Bus Vender Id | Bus vender ID for TTIA | V | V |
|  | Equipment Provider | EVSE provide vender | V | V |
|  | Transportation Company No | TTIA info transportation company id | V | V |
|  | Charge Box Id | EVSE ID for TTIA | V | V |
|  | EVSE Station | EVSE locate station | V | V |

Form 3-16 TTIA backend information item


![img_page39_0](/img/manual/img_page39_0.jpeg)

### Modbus TCP Server

|  | MODBUS Tcp Server |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Mode | Disable : Modbus TCP server shutdown. Enable:Modbus TCP server will be host on port 502 and only allow one connection in. | V | V |
|  | Password Verify | Disable : Access any modbus register directly. Enable:Before access modbus register must write password hash to password register for login | V | V |


|  | Password | 1. This effect if password verify as enable. 2. Password must hash by sha256 in lower case. | V | V |
| --- | --- | --- | --- | --- |
|  | TLS encryption | Disable : Modbus TCP in transparentcy mode Enable : Modbus TCP in TLS encrypted mode | V | V |
