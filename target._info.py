
from urllib.parse import urlparse
import socket

def get_target():
    value = input("Enter authorized domain or lab IP: ").strip()
    if "://" not in value:
        value = "//" + value

    host = urlparse(value).hostname
    if not host or any(c.isspace() for c in host):
        raise ValueError("Invalid target")

    return host

def run(target):
    try:
        ip = socket.gethostbyname(target)
    except OSError:
        ip = "DNS resolution failed"

    print(f"Target: {target}")
    print(f"Resolved IP: {ip}")
    return {"hostname": target, "ip": ip}
