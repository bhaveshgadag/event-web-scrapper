import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = os.getenv("EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == '__main__':
    test_message = f"""\
Subject: Test email

From :test@example.com
This is a test email from gmail smtp.
"""

    send_email(test_message)