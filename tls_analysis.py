
import socket
import ssl
from datetime import datetime, timezone

def run(target):
    context = ssl.create_default_context()

    try:
        with socket.create_connection((target, 443), timeout=5) as raw:
            with context.wrap_socket(raw, server_hostname=target) as tls:
                cert = tls.getpeercert()
                result = {
                    "tls_version": tls.version(),
                    "cipher": tls.cipher()[0],
                    "subject": cert.get("subject"),
                    "issuer": cert.get("issuer"),
                    "expires": cert.get("notAfter"),
                }
                print(result)
                return result

    except (OSError, ssl.SSLError) as error:
        print("TLS check failed:", error)
        return {"error": str(error)}
