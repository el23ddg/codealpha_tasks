from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP
from colorama import Fore, Style
import time

# List to store captured packets
packets = []

# Helper function to display packet details
def display_packet(packet):
    global packets

    # Add packet to the list
    packets.append(packet)

    print(Fore.CYAN + "\n[+] New Packet Captured" + Style.RESET_ALL)

    # IP Layer
    if packet.haslayer(IP):
        print(Fore.GREEN + f"IP Packet:" + Style.RESET_ALL)
        print(f"  Source IP: {packet[IP].src}")
        print(f"  Destination IP: {packet[IP].dst}")
        print(f"  TTL: {packet[IP].ttl}")

    # TCP Layer
    if packet.haslayer(TCP):
        print(Fore.YELLOW + "\n[+] TCP Packet" + Style.RESET_ALL)
        print(f"  Source Port: {packet[TCP].sport}")
        print(f"  Destination Port: {packet[TCP].dport}")
        print(f"  Flags: {packet[TCP].flags}")

    # UDP Layer
    elif packet.haslayer(UDP):
        print(Fore.MAGENTA + "\n[+] UDP Packet" + Style.RESET_ALL)
        print(f"  Source Port: {packet[UDP].sport}")
        print(f"  Destination Port: {packet[UDP].dport}")
        print(f"  Length: {packet[UDP].len}")

    # ICMP Layer
    elif packet.haslayer(ICMP):
        print(Fore.CYAN + "\n[+] ICMP Packet" + Style.RESET_ALL)
        print(f"  Type: {packet[ICMP].type}")
        print(f"  Code: {packet[ICMP].code}")

    # Delay to prevent terminal flooding
    time.sleep(0.5)

# Sniffer function
def start_sniffer():
    print(Fore.GREEN + "[+] Starting Scapy Sniffer..." + Style.RESET_ALL)
    
    # Sniff packets and call display_packet() for each one
    sniff(filter="ip or icmp or tcp or udp", prn=display_packet, store=True, count=100)

    # Save packets to .pcap file
    output_file = "captured_packets.pcap"
    wrpcap(output_file, packets)
    
    print(Fore.CYAN + f"\n[+] Packets saved to {output_file}" + Style.RESET_ALL)

# Run the sniffer
start_sniffer()
