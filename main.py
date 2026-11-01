
try:
    from target_info import get_target, run as target_info
except ModuleNotFoundError as error:
    if error.name != "target_info":
        raise

    def get_target():
        return input("Enter an authorized target: ").strip()

    def target_info(target):
        return {"target": target}
import dns_enum
import port_scan
import http_headers
import tls_analysis
import web_crawler
import tech_detect
import security_checks
import full_recon
import report

def banner():
    BURGUNDY = "\033[38;5;88m"
    RED = "\033[38;5;124m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print(f"""
{BURGUNDY}{BOLD}
██╗    ██╗███████╗██████╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔════╝╚════██╗████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝██████╔╝█████╗   █████╔╝██╔██╗ ██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══╝   ╚═══██╗██║╚██╗██║
╚███╔███╔╝███████╗██████╔╝██║  ██║███████╗██████╔╝██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝
{RESET}
{RED}{BOLD}       >>> WEB RECONNAISSANCE FRAMEWORK <<<
{WHITE}          Automated Recon | Analysis | Reporting
{BURGUNDY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{RED}  [*] Framework : {WHITE}WebReconX
{RED}  [*] Mode      : {WHITE}Authorized Security Testing
{RED}  [*] Modules   : {WHITE}DNS | PORTS | TLS | HTTP | CRAWLER
{BURGUNDY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{RESET}""")

def menu():
    print("""
[1]  Target Information
[2]  DNS Enumeration
[3]  Port Scan
[4]  HTTP Header Analysis
[5]  TLS Analysis
[6]  Web Crawler
[7]  Technology Detection
[8]  Security Checks
[9]  Full Recon
[10] Generate Report
[0]  Exit
""")

def main():
    banner()
    target = None
    results = {}

    while True:
        menu()
        choice = input("WebReconX > ").strip()

        if choice == "1":
            target = get_target()
            results["target"] = target_info(target)

        elif choice in map(str, range(2, 9)) or choice == "9":
            if not target:
                print("Select option 1 and enter an authorized target first.")
                continue

            modules = {
                "2": dns_enum.run,
                "3": port_scan.run,
                "4": http_headers.run,
                "5": tls_analysis.run,
                "6": web_crawler.run,
                "7": tech_detect.run,
                "8": security_checks.run,
                "9": full_recon.run,
            }

            try:
                results[choice] = modules[choice](target)
            except Exception as error:
                print(f"Module error: {error}")

        elif choice == "10":
            report.run(target, results)

        elif choice == "0":
            print("WebReconX closed.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()






