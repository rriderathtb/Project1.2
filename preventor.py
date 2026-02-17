import json
from firewall_manager import FirewallManager

class Preventer:
    def __init__(self):
        with open("config.json") as f:
            self.config = json.load(f)

    def handle_attack(self, attack_type, mac):
        print(f"[!] {attack_type} attack detected from {mac}")
        
        # Check if AUTO_BLOCK is enabled in config before taking action
        if self.config.get("AUTO_BLOCK", False):
            FirewallManager.block_mac(mac)
            print(f"[+] MAC {mac} successfully blocked via firewall")