
import dns_enum
import port_scan
import http_headers
import tls_analysis
import web_crawler
import tech_detect
import security_checks

def run(target):
    print("\n=== FULL RECON STARTED ===")

    modules = [
        ("dns", dns_enum.run),
        ("ports", port_scan.run),
        ("http_headers", http_headers.run),
        ("tls", tls_analysis.run),
        ("crawler", web_crawler.run),
        ("technologies", tech_detect.run),
        ("security_checks", security_checks.run),
    ]

    results = {}

    for name, function in modules:
        print(f"\n--- {name.upper()} ---")
        try:
            results[name] = function(target)
        except Exception as error:
            results[name] = {"error": str(error)}
            print("Module failed:", error)

    print("\n=== FULL RECON COMPLETE ===")
    return results
