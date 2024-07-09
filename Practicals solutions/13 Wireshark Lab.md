# Practical 13: Wireshark Lab

## Overview

This practical exercise is designed to introduce you to the Wireshark software tool, which is used for network protocol analysis. You will learn how to capture and analyze network traffic. This session will take about 30 minutes to complete.

## Task

### Part 1: Introduction to Wireshark (10 minutes)

1. **What is Wireshark?**
   - Wireshark is a network protocol analyzer that lets you capture and interactively browse the traffic running on a computer network.
   - It is used for network troubleshooting, analysis, software and protocol development, and education.

2. **Installing Wireshark:**
   - Download and install Wireshark from the official website: [Wireshark Download](https://www.wireshark.org/download.html).
   - Follow the installation instructions for your operating system.

3. **Wireshark Interface:**
   - Open Wireshark and familiarize yourself with the interface.
   - Main components include:
     - **Capture Interfaces:** List of network interfaces available for packet capture.
     - **Packet List Pane:** Displays captured packets.
     - **Packet Details Pane:** Shows details of the selected packet.
     - **Packet Bytes Pane:** Displays the raw data of the selected packet.

### Part 2: Capturing Network Traffic (10 minutes)

1. **Selecting an Interface:**
   - Open Wireshark and select the network interface you want to capture traffic on (e.g., Wi-Fi, Ethernet).
   - Click on the interface to start capturing packets.

2. **Starting a Capture:**
   - Click the "Start" button to begin capturing network traffic.
   - Perform some network activity (e.g., browse the web, check email) to generate traffic.

3. **Stopping a Capture:**
   - Click the "Stop" button to stop capturing packets.
   - Save the capture file for later analysis.

### Part 3: Analyzing Captured Traffic (10 minutes)

1. **Filtering Packets:**
   - Use Wireshark's display filter to narrow down the captured packets to specific criteria (e.g., HTTP traffic, DNS queries).
   - Example Filters:
     - `http`: Display only HTTP traffic.
     - `dns`: Display only DNS queries and responses.
     - `ip.addr == 192.168.1.1`: Display packets to or from the IP address 192.168.1.1.

2. **Inspecting Packets:**
   - Select a packet in the Packet List Pane to view its details in the Packet Details Pane.
   - Expand the protocol layers to examine the contents of each layer (e.g., Ethernet, IP, TCP, HTTP).

3. **Exporting Packets:**
   - Save the filtered packets for further analysis or reporting.
   - Go to `File > Export Specified Packets` and choose the format and location to save the packets.

### Part 4: Exercises (10 minutes)

1. **Exercise 1: Capture and Filter HTTP Traffic**


GET /en-US/livetile/preinstall?region=US&appid=C98EA5B0842DBB9405BBF071E1DA76512D21FE36&FORM=Threshold HTTP/1.1
Connection: Keep-Alive
User-Agent: Microsoft-WNS/10.0
Host: tile-service.weather.microsoft.com

HTTP/1.1 200 OK
Content-Type: application/xml; charset=utf-8
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: TicketType,RequestContinuationKey,AuthToken,Content-Type,x-client-activityid,ms-cv,OneSvc-Uni-Feat-Tun,signedInCookieName,muid,appid,User-Location,user-location,userauthtoken,usertickettype,sitename,s2sauthtoken,thumbprint,Authorization,Ent-Authorization,UserIdToken,DDD-TMPL,DDD-ActivityId,DDD-FeatureSet,DDD-Session-ID,Date,date,ads-referer,ads-referer,taboola-sessionId,taboola-sessionid,Akamai-Request-ID,Akamai-Server-IP,X-MSEdge-Ref,DDD-DebugId,s-xbox-token,OneWebServiceLatency,X-FD-Features,DDD-UserType,traceparent,Widgets,Muted,Velocity,DDD-Auth-Features,SoftLanding,PrefMigrated,DDD-TMPL-Removed,deviceFeatures
Access-Control-Allow-Methods: PUT,PATCH,POST,GET,OPTIONS,DELETE
Access-Control-Allow-Origin: *.msn.com
Access-Control-Expose-Headers: TicketType,RequestContinuationKey,AuthToken,Content-Type,x-client-activityid,ms-cv,OneSvc-Uni-Feat-Tun,signedInCookieName,muid,appid,User-Location,user-location,userauthtoken,usertickettype,sitename,s2sauthtoken,thumbprint,Authorization,Ent-Authorization,UserIdToken,DDD-TMPL,DDD-ActivityId,DDD-FeatureSet,DDD-Session-ID,Date,date,ads-referer,ads-referer,taboola-sessionId,taboola-sessionid,Akamai-Request-ID,Akamai-Server-IP,X-MSEdge-Ref,DDD-DebugId,s-xbox-token,OneWebServiceLatency,X-FD-Features,DDD-UserType,traceparent,Widgets,Muted,Velocity,DDD-Auth-Features,SoftLanding,PrefMigrated,DDD-TMPL-Removed,deviceFeatures
DDD-AuthenticatedWithJwtFlow: False
DDD-UserType: Unknown
XAP-Workflow-Version: 1.446.0
DDD-DebugId: 668ccf86-3c24-439d-9505-89b1d7a6f4d6|2024-07-09T05:49:58.4859457Z|fabric_msn|NEU1|News_211
OneWebServiceLatency: 16
X-MSEdge-ResponseInfo: 16
X-Ceto-ref: 668ccf863c24439d950589b1d7a6f4d6|AFD:668ccf863c24439d950589b1d7a6f4d6|2024-07-09T05:49:58.467Z
nel: {"report_to":"network-errors","max_age":604800,"success_fraction":0.001,"failure_fraction":1.0}
report-to: {"group":"network-errors","max_age":604800,"endpoints":[{"url":"https://deff.nelreports.net/api/report?cat=msn"}]}
X-MSEdge-Ref: Ref A: EFA167C3DA834141967507AE3AD389A7 Ref B: MIL30EDGE1309 Ref C: 2024-07-09T05:49:58Z
Date: Tue, 09 Jul 2024 06:00:20 GMT
Content-Length: 5146
Connection: keep-alive



2. **Exercise 2: Analyze DNS Queries**


Frame 31298: 249 bytes on wire (1992 bits), 249 bytes captured (1992 bits) on interface \Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D})
        Interface name: \Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D}
        Interface description: Ethernet
    Encapsulation type: Ethernet (1)
    Arrival Time: Jul  9, 2024 09:06:14.173467000 Arab Standard Time
    UTC Arrival Time: Jul  9, 2024 06:06:14.173467000 UTC
    Epoch Arrival Time: 1720505174.173467000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.048126000 seconds]
    [Time delta from previous displayed frame: 1.291089000 seconds]
    [Time since reference or first frame: -19.444145000 seconds]
    Frame Number: 31298
    Frame Length: 249 bytes (1992 bits)
    Capture Length: 249 bytes (1992 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:udp:dns]
    [Coloring Rule Name: UDP]
    [Coloring Rule String: udp]
Ethernet II, Src: Cisco_f2:5a:00 (00:1c:0e:f2:5a:00), Dst: Dell_8e:e0:e3 (90:b1:1c:8e:e0:e3)
    Destination: Dell_8e:e0:e3 (90:b1:1c:8e:e0:e3)
        Address: Dell_8e:e0:e3 (90:b1:1c:8e:e0:e3)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: Cisco_f2:5a:00 (00:1c:0e:f2:5a:00)
        Address: Cisco_f2:5a:00 (00:1c:0e:f2:5a:00)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 10.190.3.20, Dst: 10.131.16.148
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 235
    Identification: 0x23cb (9163)
    000. .... = Flags: 0x0
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 59
    Protocol: UDP (17)
    Header Checksum: 0x324f [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 10.190.3.20
    Destination Address: 10.131.16.148
User Datagram Protocol, Src Port: 53, Dst Port: 51697
    Source Port: 53
    Destination Port: 51697
    Length: 215
    Checksum: 0x4dcf [unverified]
    [Checksum Status: Unverified]
    [Stream index: 1305]
    [Timestamps]
        [Time since first frame: 1.291089000 seconds]
        [Time since previous frame: 1.291089000 seconds]
    UDP payload (207 bytes)
Domain Name System (response)
    Transaction ID: 0xc8f0
    Flags: 0x8180 Standard query response, No error
    Questions: 1
    Answer RRs: 4
    Authority RRs: 0
    Additional RRs: 0
    Queries
        edge-consumer-static.azureedge.net: type HTTPS, class IN
            Name: edge-consumer-static.azureedge.net
            [Name Length: 34]
            [Label Count: 3]
            Type: HTTPS (65) (HTTPS Specific Service Endpoints)
            Class: IN (0x0001)
    Answers
        edge-consumer-static.azureedge.net: type CNAME, class IN, cname edge-consumer-static.afd.azureedge.net
            Name: edge-consumer-static.azureedge.net
            Type: CNAME (5) (Canonical NAME for an alias)
            Class: IN (0x0001)
            Time to live: 502 (8 minutes, 22 seconds)
            Data length: 27
            CNAME: edge-consumer-static.afd.azureedge.net
        edge-consumer-static.afd.azureedge.net: type CNAME, class IN, cname azureedge-t-prod.trafficmanager.net
            Name: edge-consumer-static.afd.azureedge.net
            Type: CNAME (5) (Canonical NAME for an alias)
            Class: IN (0x0001)
            Time to live: 755 (12 minutes, 35 seconds)
            Data length: 34
            CNAME: azureedge-t-prod.trafficmanager.net
        azureedge-t-prod.trafficmanager.net: type CNAME, class IN, cname shed.dual-low.s-part-0034.t-0009.t-msedge.net
            Name: azureedge-t-prod.trafficmanager.net
            Type: CNAME (5) (Canonical NAME for an alias)
            Class: IN (0x0001)
            Time to live: 15 (15 seconds)
            Data length: 44
            CNAME: shed.dual-low.s-part-0034.t-0009.t-msedge.net
        shed.dual-low.s-part-0034.t-0009.t-msedge.net: type CNAME, class IN, cname s-part-0034.t-0009.t-msedge.net
            Name: shed.dual-low.s-part-0034.t-0009.t-msedge.net
            Type: CNAME (5) (Canonical NAME for an alias)
            Class: IN (0x0001)
            Time to live: 7 (7 seconds)
            Data length: 2
            CNAME: s-part-0034.t-0009.t-msedge.net
    [Request In: 31230]
    [Time: 1.291089000 seconds]


3. **Exercise 3: Inspect a TCP Connection**


Frame 32799: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface \Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D}, id 0
    Section number: 1
    Interface id: 0 (\Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D})
        Interface name: \Device\NPF_{50105B90-3211-4EC2-A903-4D691E346E9D}
        Interface description: Ethernet
    Encapsulation type: Ethernet (1)
    Arrival Time: Jul  9, 2024 09:08:11.469247000 Arab Standard Time
    UTC Arrival Time: Jul  9, 2024 06:08:11.469247000 UTC
    Epoch Arrival Time: 1720505291.469247000
    [Time shift for this packet: 0.000000000 seconds]
    [Time delta from previous captured frame: 0.054784000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 2232.720166000 seconds]
    Frame Number: 32799
    Frame Length: 66 bytes (528 bits)
    Capture Length: 66 bytes (528 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp]
    [Coloring Rule Name: TCP SYN/FIN]
    [Coloring Rule String: tcp.flags & 0x02 || tcp.flags.fin == 1]
Ethernet II, Src: Cisco_8a:72:80 (00:1b:90:8a:72:80), Dst: Dell_8e:e2:31 (90:b1:1c:8e:e2:31)
    Destination: Dell_8e:e2:31 (90:b1:1c:8e:e2:31)
        Address: Dell_8e:e2:31 (90:b1:1c:8e:e2:31)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: Cisco_8a:72:80 (00:1b:90:8a:72:80)
        Address: Cisco_8a:72:80 (00:1b:90:8a:72:80)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 10.136.242.31, Dst: 10.131.16.127
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 52
    Identification: 0x1295 (4757)
    010. .... = Flags: 0x2, Don't fragment
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 122
    Protocol: TCP (6)
    Header Checksum: 0xd685 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 10.136.242.31
    Destination Address: 10.131.16.127
Transmission Control Protocol, Src Port: 62910, Dst Port: 7680, Seq: 0, Len: 0
    Source Port: 62910
    Destination Port: 7680
    [Stream index: 305]
    [Conversation completeness: Incomplete, SYN_SENT (1)]
    [TCP Segment Len: 0]
    Sequence Number: 0    (relative sequence number)
    Sequence Number (raw): 1887803560
    [Next Sequence Number: 1    (relative sequence number)]
    Acknowledgment Number: 0
    Acknowledgment number (raw): 0
    1000 .... = Header Length: 32 bytes (8)
    Flags: 0x002 (SYN)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgment: Not set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ··········S·]
    Window: 64240
    [Calculated window size: 64240]
    Checksum: 0x3f89 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
        TCP Option - Maximum segment size: 1460 bytes
            Kind: Maximum Segment Size (2)
            Length: 4
            MSS Value: 1460
        TCP Option - No-Operation (NOP)
        TCP Option - Window scale: 8 (multiply by 256)
        TCP Option - No-Operation (NOP)
        TCP Option - No-Operation (NOP)
        TCP Option - SACK permitted
            Kind: SACK Permitted (4)
            Length: 2
    [Timestamps]


## Summary

- You have been introduced to the Wireshark software tool and its interface.
- You have learned how to capture network traffic using Wireshark.
- You have practiced filtering and analyzing captured traffic.
- You have completed exercises to capture and analyze HTTP, DNS, and TCP traffic.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"13 Wireshark Lab.md"` in the `"Practical Solutions"` directory.
