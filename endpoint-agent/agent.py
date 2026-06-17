import psutil
import socket
import getpass
from datetime import datetime

hostname = socket.gethostname()
username = getpass.getuser()

with open("endpoint_logs.txt", "a") as log:

    log.write("\n" + "="*50 + "\n")
    log.write(f"Time: {datetime.now()}\n")
    log.write(f"Hostname: {hostname}\n")
    log.write(f"Username: {username}\n")

    log.write("\nRunning Processes:\n")

    for proc in psutil.process_iter(['pid','name']):
        try:
            log.write(
                f"PID: {proc.info['pid']} "
                f"Process: {proc.info['name']}\n"
            )
        except:
            pass

print("Logs collected successfully")