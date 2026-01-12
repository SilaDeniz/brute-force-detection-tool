import json
from datetime import datetime, timedelta
import os

# --- CONFIG LOAD ---
with open("config.json", "r") as config_file:
    config = json.load(config_file)

LOG_FILE = config["log_file"]
THRESHOLD = config["threshold"]
TIME_WINDOW_MINUTES = config["time_window_minutes"]
OUTPUT_DIR = config["output_directory"]

def detect_bruteforce():
    attempts = {}

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" not in line:
                continue

            parts = line.split()
            timestamp_str = " ".join(parts[0:3])
            ip = parts[parts.index("from") + 1]

            timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
            attempts.setdefault(ip, []).append(timestamp)

    alerts = []

    for ip, times in attempts.items():
        times.sort()
        for i in range(len(times)):
            window = [
                t for t in times
                if times[i] <= t <= times[i] + timedelta(minutes=TIME_WINDOW_MINUTES)
            ]
            if len(window) >= THRESHOLD:
                alerts.append({
                    "ip": ip,
                    "failed_attempts": len(window),
                    "time_window_minutes": TIME_WINDOW_MINUTES,
                    "bruteforce_detected": True
                })
                break

    return alerts


def write_report(alerts):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"{OUTPUT_DIR}/report_{timestamp}.json"

    with open(report_path, "w") as f:
        json.dump(alerts, f, indent=4)

    return report_path


if __name__ == "__main__":
    results = detect_bruteforce()

    if not results:
        print("No brute-force activity detected.")
    else:
        print("Brute-force activity detected!")
        report = write_report(results)
        print(f"Report written to: {report}")
