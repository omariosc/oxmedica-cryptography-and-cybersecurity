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
   - TODO: Start a capture on your network interface. DONE.
   - TODO: Open a web browser and visit a website. DONE.
   - TODO: Stop the capture and apply a filter to display only HTTP traffic. DONE.
   - TODO: Save the filtered packets to a file. DONE.

2. **Exercise 2: Analyze DNS Queries**
   - TODO: Start a capture on your network interface. DONE.
   - TODO: Perform a DNS query by visiting a website or using the `nslookup` command. DONE.
   - TODO: Stop the capture and apply a filter to display only DNS traffic. DONE.
   - TODO: Identify the DNS query and response packets DONE.

3. **Exercise 3: Inspect a TCP Connection**
   - TODO: Start a capture on your network interface. DONE.
   - TODO: Establish a TCP connection by visiting a website or using a network application. DONE.
   - TODO: Stop the capture and apply a filter to display only TCP traffic. DONE.
   - TODO: Inspect the TCP handshake process (SYN, SYN-ACK, ACK) for the connection. DONE.

## Summary

- You have been introduced to the Wireshark software tool and its interface.
- You have learned how to capture network traffic using Wireshark.
- You have practiced filtering and analyzing captured traffic.
- You have completed exercises to capture and analyze HTTP, DNS, and TCP traffic.

## Submission

- Complete the exercises and ensure all solutions are documented.
- Save your progress and ensure all solutions are documented and submitted to GitHub.
- Save the file with the name `"13 Wireshark Lab.md"` in the `"Practical Solutions"` directory.
