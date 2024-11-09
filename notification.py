import os

def abcd(title, message):
    try:
        os.system(f"termux-notification --title {title} --content  {message}"
        )
        print("Notification sent successfully.")
    except Exception as e:
        print("error")

abcd("Hello", " World")
