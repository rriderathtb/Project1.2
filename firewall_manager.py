import subprocess

class FirewallManager:
    @staticmethod
    def block_mac(mac):
        # Creates a unique rule name for each blocked MAC
        rule_name = f"PreventX_Block_{mac.replace(':','_')}"
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteMAC={mac}'
        subprocess.run(cmd, shell=True)

    @staticmethod
    def disable_wifi():
        subprocess.run("netsh interface set interface Wi-Fi admin=disabled", shell=True)