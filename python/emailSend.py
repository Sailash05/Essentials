import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email sender and receiver details
sender_email = "sailashs2005@gmail.com"
receiver_email = "s.sailash2005@gmail.com"
sender_password = "ljur dmec poog hdxc"  # For security, use environment variables for passwords

# Create the email subject, body, and sender/receiver details
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

# Body of the email
body = "Hello, this is a test email sent using Python."
message.attach(MIMEText(body, "plain"))

# Connecting to Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Start TLS (Transport Layer Security) for security
    server.login(sender_email, sender_password)  # Login to the server

    # Convert the message to a string and send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
