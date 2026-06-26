# detections/suspicious_process.py

process_name = "wireshark.exe"

suspicious_tools = [
    "wireshark.exe",
    "nmap.exe",
    "nc.exe",
    "metasploit.exe"
]

if process_name.lower() in suspicious_tools:
    print("[ALERT] Suspicious process detected")