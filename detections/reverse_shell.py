# detections/reverse_shell.py

commands = [
    "bash -i",
    "nc -e",
    "powershell -nop"
]

log_data = "bash -i"

for cmd in commands:
    if cmd in log_data:
        print("[ALERT] Reverse shell behavior detected")