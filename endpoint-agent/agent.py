import psutil
import time

while True:
    with open("endpoint_logs.txt", "a") as log:
        log.write("\n===== Process Snapshot =====\n")

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                log.write(
                    f"PID: {proc.info['pid']} | "
                    f"Process: {proc.info['name']}\n"
                )
            except:
                pass

    print("Logs collected successfully")
    time.sleep(30)