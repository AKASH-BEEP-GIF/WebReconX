
import urllib.request
import urllib.error

def run(target):
    request = urllib.request.Request(
        f"https://{target}/",
        headers={"User-Agent": "WebReconX-Lab/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            headers = response.headers
            server = headers.get("Server", "Not disclosed")
            powered_by = headers.get("X-Powered-By", "Not disclosed")

            result = {
                "server": server,
                "powered_by": powered_by,
                "content_type": headers.get("Content-Type", "Unknown"),
            }

            print("Technology clues:", result)
            return result

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print("Detection failed:", error)
        return {"error": str(error)}
