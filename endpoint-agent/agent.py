import psutil
from datetime import datetime

with open("endpoint_logs.txt", "w") as f:

    f.write(f"Time: {datetime.now()}\n")

    f.write("\n=== Running Processes ===\n")

    for process in psutil.process_iter():
        try:
            f.write(process.name() + "\n")
        except:
            pass

    f.write("\n=== CPU Usage ===\n")
    f.write(str(psutil.cpu_percent()) + "\n")

    f.write("\n=== Memory Usage ===\n")
    f.write(str(psutil.virtual_memory().percent) + "\n")

    f.write("\n=== Open Ports ===\n")

    for conn in psutil.net_connections():
        try:
            f.write(str(conn.laddr.port) + "\n")
        except:
            pass

print("Endpoint logs generated successfully!")