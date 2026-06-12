suspicious_processes = [
    "mimikatz.exe",
    "nc.exe",
    "ncat.exe",
    "netcat.exe",
    "powersploit.exe"
]

log_file = "../endpoint-agent/endpoint_logs.txt"

with open(log_file, "r", errors="ignore") as f:
    logs = f.readlines()

for line in logs:
    for proc in suspicious_processes:
        if proc.lower() in line.lower():
            print(f"[ALERT] Suspicious Process Detected: {proc}")
            print(line)