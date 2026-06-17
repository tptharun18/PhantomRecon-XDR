import os

suspicious = [
    "mimikatz",
    "nc.exe",
    "nmap",
    "metasploit"
]

logfile = "../endpoint-agent/endpoint_logs.txt"

if os.path.exists(logfile):

    with open(logfile, "r", errors="ignore") as f:
        data = f.read().lower()

    for item in suspicious:
        if item in data:
            print(f"[ALERT] Suspicious tool detected: {item}")