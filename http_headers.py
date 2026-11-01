
import urllib.request
import urllib.error

def run(target):
    url = f"https://{target}/"
    request = urllib.request.Request(
        url, method="HEAD",
        headers={"User-Agent": "WebReconX-Lab/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            headers = dict(response.headers.items())
            print("HTTP status:", response.status)
            for name, value in headers.items():
                print(f"{name}: {value}")
            return {"status": response.status, "headers": headers}

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print("HTTPS header request failed:", error)
        return {"error": str(error)}
