import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender_email = "veenasa676@gmail.com"
receiver_emails = ["www.chintucom644@gmail.com", "suryanshuverma09@gmail.com"]
subject = "Offer for Internship"
body = "Hi, there I am happy to hire your as an intern in our company.Welcome to Dream Company."

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "veenasa676@gmail.com"
smtp_password = os.environ.get("PASSWORD")

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to SMTP server and send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_emails, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", e)
finally:
    server.quit()


print("SMTP Password:", smtp_password)
