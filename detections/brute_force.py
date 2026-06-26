# detections/brute_force.py

failed_logins = 15

if failed_logins > 10:
    print("[ALERT] Possible brute force attack detected")