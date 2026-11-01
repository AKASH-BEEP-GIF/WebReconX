
import json
import os
from datetime import datetime

def run(target, results):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/recon_{timestamp}.json"

    report_data = {
        "target": target,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "results": results,
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report_data, file, indent=4, default=str)

    print(f"Report saved: {filename}")
    return filename
