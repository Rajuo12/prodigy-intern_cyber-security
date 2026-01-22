# Network Packet Analyzer (Tkinter + Scapy)

A compact GUI packet sniffer that uses Scapy to capture IPv4 packets and displays basic info in a Tkinter scrolled text area.

Quick summary
- Shows Source IP, Destination IP, Protocol (TCP/UDP/ICMP/Other), and a short hex payload preview.
- Start/Stop buttons; sniffing runs in a background thread so the UI stays responsive.

Requirements
- Python 3.8+
- scapy (`pip install scapy`)
- Tkinter (usually included)
- Elevated privileges to capture packets (root / Administrator). On Windows, install Npcap.

Run
- Save as `packet_analyzer.py` and run with appropriate privileges:
  - macOS/Linux: `sudo python packet_analyzer.py`
  - Windows: run as Administrator

Security & legal
- Packet capture can expose sensitive data. Only run on networks/devices you own or have permission to monitor. Follow laws and policies.

Notes & tips
- To reduce noise, add a BPF filter (e.g., `sniff(filter="tcp port 80", ...)`) or select an interface.
- For heavy traffic, batch UI updates or log to a file/PCAP to avoid slowdown.
- If Scapy or permissions fail, verify installation and run context (Npcap on Windows; `python3-tk` on Debian/Ubuntu for Tkinter).

Minimal example
The app captures packets and appends formatted summaries to the display area (see script supplied with this README).

License
MIT — use responsibly.