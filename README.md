# CodeAlpha Cybersecurity Internship Projects
## 🛡️ Python Network Sniffer with .pcap Export - Task 1
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

## 🔒 Secure Code Review: Flask Application with Python and HTML - Task 2
### 🚀 Project Overview
#### This project demonstrates secure coding practices by building a Flask application with the following functionalities:
- User Registration & Login
- Flask-Bcrypt for secure password hashing
- SQLAlchemy ORM to prevent SQL injection
- Static Code Analysis using Bandit and Flake8 for identifying security issues
### Technologies Used
- Python: v3.12
- Flask: Micro web framework
- Flask-Bcrypt: For hashing passwords
- SQLite: Database for storing user data
- SQLAlchemy: ORM for secure database interactions
- Bandit: Static security analysis tool
- Flake8: Python linting tool
### Installation and Execution
- Install dependencies
```bash
  pip install flask flask-bcrypt flask-sqlalchemy bandit flake8
```
- Initialize the Database in the terminal by going to the path where the project folder is
```bash
   flask shell  
>>> from app import db  
>>> db.create_all()  
>>> exit()  
```
- Run the Flask app in VS code
- Access the app in your browser at:
```cpp
   http://127.0.0.1:5000
```
### 🔥 Tests Performed
#### Flask-Bcrypt Testing
1. Verified that passwords were securely hashed before being stored in the database.
2. Used Flask shell to query and verify that the password was saved as a hashed string, not in plaintext.
3. Test Steps:
- Registered a user through the web interface.
- Opened Flask shell and queried the user table to confirm the hashed password.





