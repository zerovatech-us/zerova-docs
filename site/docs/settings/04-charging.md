---
id: charging
title: "3.1.2 Charging"
sidebar_position: 2
---


## 3.1.2. Charging


![img_page17_0](/img/manual/img_page17_0.jpeg)


![img_page18_0](/img/manual/img_page18_0.png)

### Charging Relevant Parameters

|  | Charging Relevant Parameters |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Max Charging Energy | The maximum charging energy per charge, charger will stop charging if present output energy reach to this threshold 0:no limit 1~65535 KWH | V | V |
|  | Max Charging Power | The maximum charging power for each charge 0:Rating value 1~rating value kW | V | V |
|  | Max Charging Current | The maximum charging current for each DC charge 0:Rating value 1~rating value Amp | V | V |
|  | AC Max Charging Current | The maximum charging current for AC gun on DC charge 0:Rating value | V | V |


|  |  | 1~rating value Amp |  |  |
| --- | --- | --- | --- | --- |
|  | Max Charging Duration | The maximum charging duration for each charge 0:no limit 1~65535 minutes | V | V |
|  | Stop Charging By Button | The state of stopping charging button - disable - enable | V | V |
|  | LocalWhiteCard0 \| LocalWhiteCard9 | This array stores the ID of administrator RFID card, charger will bypass the user authentication if administrator RFID card be swiped. | V | V |
|  | 15118 | ISO-15118 feature support | V | V |
|  | PnC | PnC feature support | V | V |
|  | Contract Install/Update | PnC contract install/update feature support | V | V |
|  | VDV261 | Share network to EV by charging cable | V | V |
|  | VDV261 Customized Ipv6 Address | VDV261 customization IPv6 address for EV usage | V | V |
|  | VDV261 Customized Ipv6 Gateway | VDV261 customization IPv6 gateway for EV usage | V | V |
|  | VDV261 Customized Ipv6 Dns | VDV261 customization IPv6 DNS for EV usage | V | V |
|  | Multi Connector Charging Mode | Synchronous: Whole connector charging at same time Sequential: First in First out | V | V |
|  | R2R | Charging session restart by CP BCB toggle. | V | V |
|  | Billing | Using billing mode or not | V | V |
|  | Currency | Choosing currency when using billing mode | V | V |
|  | Fee0 \| Fee23 | This array stores the fee with every hours. | V | V |


Form 3-5 Charging Configuration item

![img_page20_0](/img/manual/img_page20_0.png)

Image 3-5 Charging information page

### Charging Information

Each partial information display depend on CHARGER model name.

|  | Field Name | Description | Attributes |  |
| --- | --- | --- | --- | --- |
|  |  |  | Read | Write |
|  | User Id | The user use this ID to trigger charging event, it can be RFID card number, OCPP IdTag, etc. | V |  |
|  | Star tDate Time | Charging cycle start time | V |  |
|  | Stop Date Time | Charging cycle stop time | V |  |
|  | System Status | CHARGER system present status | V |  |
|  | Connector Temperature | Connector temperature Unit:˚C | V |  |
|  | Present Charging Current | Present charging current Unit:A | V |  |
|  | Present Charging Power | Present charging power Unit:KW | V |  |
|  | Present Charged Energy | Present charging energy Unit:KWh | V |  |
|  | Present Charged Duration | Present charging duration Unit:second | V |  |
|  | Ev Battery Max Voltage | EV battery maximum voltage | V |  |
|  | Ev Battery Target Voltage | EV battery target voltage | V |  |
|  | Ev Battery Soc | Present EV battery SOC | V |  |
|  | Totalize Power Comsumption | Totalize Power Comsumption Unit:KWh | V |  |


![img_page22_0](/img/manual/img_page22_0.png)

### V2G Certificate

|  | V2G certificate |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | V2G Private Key | Private key for encrypt message between EVSE/EV, key type is ECDSA and format is x509. |  | V |
|  | V2G Certificate Chain | Certificate chain for decrypt message between EVSE/EV, certificate chain format is x509. |  | V |
|  | V2G Root Certificate | RootCA for verify certificate chain which come from EV side, CA format is x509. |  | V |
|  | MO Root Certificate | Mobility operator certificate for verify MO-sub certificate which come from EV. |  | V |
