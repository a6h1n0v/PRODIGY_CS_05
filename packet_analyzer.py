from scapy.all import sniff, conf, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        
        if packet.haslayer("Raw"):
            print(f"Payload: {packet.getlayer('Raw').load}")
        print("\n" + "-"*50 + "\n")

def main():
    print("Starting Network Packet Analyzer...")
    conf.L3socket
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
