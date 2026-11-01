
import urllib.request
import urllib.error

RECOMMENDED_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
]

def run(target):
    request = urllib.request.Request(
        f"https://{target}/",
        headers={"User-Agent": "WebReconX-Lab/1.0"}
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            headers = response.headers
            checks = {}

            for name in RECOMMENDED_HEADERS:
                checks[name] = (
                    "present" if headers.get(name) else "missing"
                )
                print(f"{name}: {checks[name]}")

            return {
                "https_reachable": True,
                "http_status": response.status,
                "security_headers": checks,
            }

    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print("Security check failed:", error)
        return {"https_reachable": False, "error": str(error)}
