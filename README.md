# Network Packet Analyzer

This repository contains a Python-based Network Packet Analyzer tool that captures and analyzes network packets. The tool displays relevant information such as source and destination IP addresses, protocols, and payload data. It is designed for educational purposes and should be used ethically.

## Features

- **Packet Sniffing**:
  - Captures live network traffic.
  - Analyzes packets to extract and display:
    - Source IP Address.
    - Destination IP Address.
    - Protocol used.
    - Packet payload data (if available).
  
- **Supports Layer 3 Packet Capture**:
  - Compatible with Windows using `Npcap` in WinPcap API-compatible mode.
  
## Prerequisites

- Python 3.x
- Install the required Python packages:
  ```bash
  pip install scapy

## Running The Script

1. **Clone The Repository**
   ```bash
   git clone https://github.com/a6h1n0v/PRODIGY_CS_05.git
   cd PRODIGY_CS_05

2. **Running The Script**
   ```bash
   python packet_analyzer.py


# Usage

### Starting the Analyzer:
- Run the script as shown above to start capturing and analyzing network packets.

### Analyzing the Output:
- The output will display packet summaries, including:
  - Source and destination IP addresses.
  - Protocol type.
  - Payload data (if available).

### Stopping the Analyzer:
- Stop the script using `Ctrl+C` when you're done capturing packets.

# Ethical Considerations

### Legal Usage:
- This tool is intended for educational purposes only. Ensure that you have proper authorization before capturing or analyzing network traffic.

### Privacy:
- Respect the privacy of others. Do not use this tool to intercept or analyze private data without permission.

