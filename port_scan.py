
import socket

PORTS = [21, 22, 25, 53, 80, 443, 445, 3306, 5000, 8080]

def run(target):
    results = {}

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror as error:
        print("Cannot resolve target:", error)
        return {"error": str(error)}

    for port in PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                status = sock.connect_ex((ip, port))
                state = "open" if status == 0 else "closed/filtered"
                results[port] = state
                print(f"{port:5} : {state}")
        except OSError as error:
            results[port] = f"error: {error}"

    return results
