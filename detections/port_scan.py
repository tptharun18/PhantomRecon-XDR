# detections/port_scan.py

import psutil

open_ports = []

for conn in psutil.net_connections():
    if conn.laddr:
        open_ports.append(conn.laddr.port)

print("Open ports:", open_ports)

if len(open_ports) > 20:
    print("[ALERT] Possible port scanning activity detected!")