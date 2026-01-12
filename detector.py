from datetime import datetime, timedelta

LOG_FILE = "sample_logs/auth.log"
THRESHOLD = 5
TIME_WINDOW_MINUTES = 1

def detect_bruteforce_with_time_window():
    attempts = {}

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" not in line:
                continue

            parts = line.split()
            timestamp_str = " ".join(parts[0:3])  # Jan 10 12:01:22
            ip = parts[parts.index("from") + 1]

            timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")

            attempts.setdefault(ip, []).append(timestamp)

    print("=== BRUTE-FORCE DETECTION (TIME WINDOW) ===")

    for ip, times in attempts.items():
        times.sort()

        for i in range(len(times)):
            window = [t for t in times if times[i] <= t <= times[i] + timedelta(minutes=TIME_WINDOW_MINUTES)]

            if len(window) >= THRESHOLD:
                print(f"[ALERT] {ip} -> {len(window)} attempts within {TIME_WINDOW_MINUTES} minute(s)")
                break


if __name__ == "__main__":
    detect_bruteforce_with_time_window()
