import os
import time
from datetime import datetime

def capture_packets(interface, duration, output_dir):
    while True:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        pcap_file = os.path.join(output_dir, f"capture_{timestamp}.pcap")
        os.system(f"tcpdump -i {interface} -G {duration} -W 1 -w {pcap_file}")

if __name__ == "__main__":
    INTERFACE = "eth0"  # Interface to capture packets
    DURATION = 60  # Capture duration in seconds
    OUTPUT_DIR = "/var/www/html/captures"  # Directory to store the

    capture_packets(INTERFACE, DURATION, OUTPUT_DIR)
