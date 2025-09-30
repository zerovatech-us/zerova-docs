# OCPP Backend

![Download Log Screenshot](img/ocpp_backend.jpeg)

| Field Name                  | Description                                                                                                                   | Attributes |     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------|-----|
|                             |                                                                                                                               | **Read**   | **Write** |
| **Ocpp Connection**         |                                                                                                                               |            |     |
| Status                      | The connection status of OCPP backend                                                                                         | V          |     |
| Central System URL          | The OCPP server URL (including port) to which the charger connects.<br/>- `ws://` non-secure OCPP 1.6-J<br/>- `wss://` secure OCPP 1.6-J<br/>Example:<br/>`ws://ocpp.phihong.com.tw:80/`<br/>`wss://ocpp.phihong.com.tw:443/` | V          | V   |
| Charge BoxId                | The Charge Box ID used to connect to the OCPP server                                                                          | V          | V   |
| Charge Point Vendor         | Charger vendor name                                                                                                           | V          | V   |
| Ocpp Security Profile       | OCPP security options:<br/>- None security<br/>- Unsecured Transport with Basic Authentication<br/>- TLS with Basic Authentication<br/>- TLS with Client Side Certificates | V | V |
| Ocpp Security Password      | Displayed when profile is:<br/>- Unsecured Transport with Basic Authentication<br/>- TLS with Basic Authentication            | V          | V   |
| Receipt URL                 | Receipt QR code URL. If filled, at session end LCM displays QR Code for user to scan and get receipt info                      | V          | V   |
| **Maintain Server**         |                                                                                                                               |            |     |
| Connection Status           | The connection status of maintain backend                                                                                     | V          |     |
| Maintain Server URL         | The maintain server URL (including port) to which the charger connects.<br/>- `ws://` non-secure OCPP 1.6-J<br/>- `wss://` secure OCPP 1.6-J<br/>Example:<br/>`ws://ocpp.phihong.com.tw:80/`<br/>`wss://ocpp.phihong.com.tw:443/` | V | V |
| Maintain Server Security Profile | Maintain server security options:<br/>- None security<br/>- Unsecured Transport with Basic Authentication<br/>- TLS with Basic Authentication | V | V |