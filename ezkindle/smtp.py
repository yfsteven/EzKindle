import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv

def send_mail(attachment):
    try:
        load_dotenv()

        sender_email = getenv('SENDER_EMAIL')
        kindle_email = getenv('KINDLE_EMAIL')
        app_password = getenv('APP_PASSWORD')

        PORT = 465
        smtp_server = 'smtp.gmail.com'

        msg = MIMEMultipart()
        msg['Subject'] = 'Sent by EzKindle'
        msg['From'] = sender_email
        msg['To'] = kindle_email

        with open(attachment,'rb') as file:
            content = file.read()

        attachment = MIMEApplication(content, Name=attachment)
        msg.attach(attachment)

        with smtplib.SMTP_SSL(smtp_server, PORT) as server:
           server.login(sender_email, app_password)
           server.sendmail(sender_email, kindle_email, msg.as_string())
    except Exception as err:
        print(f"Something went wrong - {err}")
