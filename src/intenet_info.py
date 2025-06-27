
import os

# ALL CODE HERE IS SHIT, DO NOT TRUST THE CODE, ONLY THE FILE NAMES LOL

def get_default_interface():
    with os.popen("ip route | grep default") as f:
        for line in f:
            parts = line.split()
            if "dev" in parts:
                return parts[parts.index("dev") + 1]
    return None

def get_interface_bytes(interface="eth0"):
    with open("/proc/net/dev") as f:
        for line in f:
            if interface in line:
                parts = line.split(f"{interface}:")[1].split()
                rx_bytes = int(parts[0])
                tx_bytes = int(parts[8])
                return rx_bytes, tx_bytes
    return None, None

iface = get_default_interface()
print(f"Default interface: {iface}")

rx, tx = get_interface_bytes(iface)

if rx is None or tx is None:
    print(f"Interface '{iface}' not found.")
else:
    print(f"Received: {rx / (1024**2):.2f} MB, Sent: {tx / (1024**2):.2f} MB")