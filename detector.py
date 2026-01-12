LOG_FILE = "sample_logs/auth.log"

def count_failed_logins_by_ip():
    ip_counts = {}

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[parts.index("from") + 1]

                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

    return ip_counts


if __name__ == "__main__":
    results = count_failed_logins_by_ip()

    print("=== FAILED LOGIN COUNT BY IP ===")
    for ip, count in results.items():
        print(f"{ip} -> {count} failed attempts")
