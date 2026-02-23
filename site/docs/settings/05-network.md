---
id: network
title: "3.1.3 Network"
sidebar_position: 3
---

## 3.1.3. Network


![img_page23_0](/img/manual/img_page23_0.png)

Image 3-7 Network status information page

### Network Status

| Network Status |  |  |  |
| --- | --- | --- | --- |
| Field Name | Description | Attributes |  |
|  |  | Read | Write |
| Internet Connection Status | CHARGER internet connection status | V |  |

Form 3-8 Network status information item


![img_page24_0](/img/manual/img_page24_0.jpeg)

### Ethernet Interface

|  | Ethernet Interface |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Dhcp Client | Ethernet DHCP client ability selection | V | V |
|  | Mac Address | Ethernet MAC address | V |  |
|  | Ip Address | Ethernet IP address | V | V |
|  | Submask Address | Ethernet submask address | V | V |
|  | Gateway Address | Ethernet gateway address | V | V |
|  | Wifi to Ethernet | Bridge ethernet as lan port of WIFI | V | V |


| Bridge | AP |  |  |
| --- | --- | --- | --- |
| NAT 4G Interface | Select interface to share internet connection ability Ppp0: 1st 4G module Ppp1: 2nd 4G module | V | V |

Form 3-9 Ethernet information item


![img_page26_0](/img/manual/img_page26_0.png)

Image 3-9 Wifi module information page

### WiFi Module

|  | WiFi Module |  |  |  |
| --- | --- | --- | --- | --- |
|  | Field Name | Description | Attributes |  |
|  |  |  | Read | Write |
|  | Mode | Wi-Fi module mode - Disable - Station - Access Point | V | V |
|  | SSID | 1. AP:Fix use modelname & SN 2. Station:Target connect SSID | V | V |
|  | Password | The password or preshare key for client to do login | V | V |
|  | Client EAP-TLS Identity | WPA enterprise EAP-TLS login identity | V | V |
|  | Client EAP-TLS private key | WPA enterprise EAP-TLS login private key |  | V |
|  | Client EAP-TLS certificate | WPA enterprise EAP-TLS login certificate |  | V |
|  | Client EAP-TLS root certificate | WPA enterprise EAP-TLS login root certificate |  | V |
|  | Wifi Target Bssid Mac | Bonding AP MAC address Sample: AA:BB:CC:DD:EE:FF | V | V |
|  | RSSI | the received signal strength of WiFi connection | V |  |
|  | Dhcp Server | DHCP server will be ran under infrastructure server mode if enabled | V | V |
|  | DhcpClient | DHCP client will be ran via WiFi module if enabled | V | V |
|  | Mac Address | Wi-Fi MAC address | V |  |
|  | Ip Address | Wi-Fi IP address | V | V |
|  | Submask Address | Wi-Fi submask address | V | V |
|  | Gateway Address | Wi-Fi gateway address | V | V |
|  | Network Connection Status | Wi-Fi network connection status | V |  |

Form 3-10 WiFi module information item


![img_page28_0](/img/manual/img_page28_0.png)

Image 3-10 3G/4G module information page

### 3G/4G Module

|  | Field Name | Description | Attributes |  |
| --- | --- | --- | --- | --- |
|  |  |  | Read | Write |
|  | Mode | Telecom module mode - Disable - Enable | V | V |
|  | APN | The APN which charger want to connected | V | V |
|  | Network Type | -Auto -4G -3G -2G | V | V |
|  | Rssi | The signal strength of 3G/4G connection | V |  |
|  | Chap Pap Id | The login ID for CHAP/PAP authentication | V | V |
|  | Chap Pap Pwd | The login password for CHAP/PAP authentication | V | V |
|  | Modem IMEI | The IMEI code of this telcom modem | V |  |
|  | SIM IMSI | The IMSI code of this SIM card | V |  |
|  | SIM ICCID | Telcom SIM ICCID | V |  |
|  | SIM Status | Present SIM card status | V |  |
|  | Modem Mode | Present telcom system mode through this modem | V |  |
|  | IP Address | Telcom IP address | V |  |
|  | Network Connection Status | Telcom network connection status | V |  |


![img_page30_0](/img/manual/img_page30_0.png)

Image 3-11 Firewall information page

### Firewall

|  | Field Name | Description | Attributes |  |
| --- | --- | --- | --- | --- |
|  |  |  | Read | Write |
|  | Mode | Firewall module mode - Disable - Enable, deny all packet except charger build-in use server address and address on white list. | V | V |
|  | Firewall Accept Addr0 | Server address whitelist 0 | V | V |
|  | Firewall Accept Addr1 | Server address whitelist 1 | V | V |
|  | Firewall Accept Addr2 | Server address whitelist 2 | V | V |
|  | Firewall Accept Addr3 | Server address whitelist 3 | V | V |
|  | Firewall Accept Addr4 | Server address whitelist 4 | V | V |
|  | Firewall Accept Addr5 | Server address whitelist 5 | V | V |
|  | Firewall Accept Addr6 | Server address whitelist 6 | V | V |
|  | Firewall Accept Addr7 | Server address whitelist 7 | V | V |
|  | Firewall Accept Addr8 | Server address whitelist 8 | V | V |
|  | Firewall Accept Addr9 | Server address whitelist 9 | V | V |
