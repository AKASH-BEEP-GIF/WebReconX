
import socket

def run(target):
    results = {}
    try:
        for item in socket.getaddrinfo(target, None):
            family = item[0]
            address = item[4][0]
            version = "IPv6" if family == socket.AF_INET6 else "IPv4"
            results.setdefault(version, set()).add(address)

        results = {k: sorted(v) for k, v in results.items()}
        print("DNS results:", results)
    except socket.gaierror as error:
        results = {"error": str(error)}
        print(results)

    return results
