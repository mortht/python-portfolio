import smtplib, ssl, os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("GMAIL_USERNAME")
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = os.getenv("RECEIVER")
    if not receiver:
        receiver = username

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)