import psutil
import time
from datetime import datetime

LOG_FILE = "endpoint_logs.txt"

while True:
    processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(
                f"{datetime.now()} | PID:{proc.info['pid']} | {proc.info['name']}"
            )
        except:
            pass

    with open(LOG_FILE, "a") as f:
        for p in processes:
            f.write(p + "\n")

    print(f"Collected {len(processes)} processes")

    time.sleep(10)