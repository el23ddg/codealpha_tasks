# CodeAlpha Cybersecurity Internship Projects
## 🛡️ Python Network Sniffer with .pcap Export
A simple Python-based network sniffer that captures and displays TCP, UDP, ICMP, and IP packets in real-time. It also saves the captured packets into a .pcap file for Wireshark analysis.
### 🔥 Features
- 🛠️ Captures all major protocols → TCP, UDP, ICMP, and IP packets.
- 🎨 Color-coded output → Clear and readable terminal output.
- 📄 Exports to .pcap → Save packets for further analysis in Wireshark.
- ⏱️ Controlled packet capturing → Captures a set number of packets and saves them automatically.
### Libraries Used
- scapy
- colorama
```bash
  pip install scapy
  pip install colorama
```
### 🚀 Usage
#### 💻 Run the Sniffer
- The sniffer will capture 100 packets and save them to a .pcap file.
- You can modify the number of packets by changing: count = 100
#### 🌐 Testing the Sniffer
#### Open another terminal and generate some network traffic:
```bash
 ping google.com               # ICMP packet  
 curl http://example.com       # TCP packet  
 nslookup example.com          # UDP packet
```
### 📄 Output (terminal and wireshark)
![Screenshot 2025-03-29 001256](https://github.com/user-attachments/assets/2a2f563b-85aa-47d8-8fee-dca6d12f9acd)
![Screenshot 2025-03-29 001520](https://github.com/user-attachments/assets/88377afd-a624-4bab-afd0-5f07d7d29ee0)
### 🔍 Analyze the Packets in Wireshark
- Open Wireshark.
- Go to File → Open.
- Select the captured_packets.pcap file.
- Analyze the captured packets with filters, detailed protocol info, and visualizations.
### 🔥 Customization Ideas (add more features)
- Filtering by specific protocols or IP addresses.
- Adding payload analysis to display raw packet data.
- Running the sniffer continuously by removing the count limit.
- Exporting logs to a text or CSV file for further analysis.










