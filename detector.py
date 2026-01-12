LOG_FILE = "sample_logs/auth.log"

def get_failed_logins():
    failed_lines = []

    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line:
                failed_lines.append(line.strip())

    return failed_lines


if __name__ == "__main__":
    failed_logins = get_failed_logins()

    print("=== FAILED LOGIN ATTEMPTS ===")
    for log in failed_logins:
        print(log)
