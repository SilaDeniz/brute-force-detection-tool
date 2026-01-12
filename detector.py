LOG_FILE = "sample_logs/auth.log"

def read_log_file():
    with open(LOG_FILE, "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    read_log_file()
