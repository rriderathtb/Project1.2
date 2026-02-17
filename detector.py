from scapy.all import Dot11Deauth, EAPOL, sniff
import json
from logger import Logger
from preventor import Preventer

class Detector:
    def __init__(self):
        with open("config.json") as f:
            self.config = json.load(f)
        
        self.deauth_count = {}
        self.bruteforce_attempts = {}
        self.logger = Logger()
        self.preventer = Preventer()

    def process_packet(self, pkt):
        # 1. Detect Deauthentication Attacks
        if pkt.haslayer(Dot11Deauth):
            mac = pkt.addr2
            self.deauth_count[mac] = self.deauth_count.get(mac, 0) + 1
            if self.deauth_count[mac] >= self.config["DEAUTH_THRESHOLD"]:
                self.logger.log("DEAUTH", mac, "Threshold exceeded")
                self.preventer.handle_attack("DEAUTH", mac)

        # 2. Detect EAPOL (WPA Handshake) Brute Force
        if pkt.haslayer(EAPOL):
            mac = pkt.addr2
            self.bruteforce_attempts[mac] = self.bruteforce_attempts.get(mac, 0) + 1
            if self.bruteforce_attempts[mac] >= self.config["BRUTEFORCE_THRESHOLD"]:
                self.logger.log("BRUTEFORCE", mac, "Repeated EAPOL frames")
                self.preventer.handle_attack("BRUTEFORCE", mac)

    def start(self, interface="Wi-Fi"):
        # The prn argument connects the sniffer to the processing logic
        sniff(iface=interface, prn=self.process_packet, store=False)