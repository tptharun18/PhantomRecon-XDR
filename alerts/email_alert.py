import yagmail

sender_email = "tptharun30@gmail.com"
app_password = "wqkk lphq xvvk kbmg"

receiver_email = "juug23betech15621@gmail.com"

yag = yagmail.SMTP(sender_email, app_password)

yag.send(
    to=receiver_email,
    subject="🚨 PhantomRecon XDR Alert",
    contents="""
Threat Type : Reverse Shell
Severity    : HIGH

Action Recommended:
Investigate immediately.
"""
)

print("Email alert sent successfully!")