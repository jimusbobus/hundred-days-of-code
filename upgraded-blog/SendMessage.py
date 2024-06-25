from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.header import Header

SMS_NUMBER = "+447441368107"
SMS_SID = "AC958b6ac8e38724bbe258b079122cc63a"
SMS_AUTH_ID = "725fbbd9420a93e6b6cf2906081dbcfc"
SMTP_USER = "jimusbobus@gmail.com"
SMTP_PASSWORD = "mmsa ujxr tcas dhvq"


def send_sms(msg, to='07803605128'):
    client = Client(SMS_SID, SMS_AUTH_ID)
    message = client.messages.create(body=msg, from_=SMS_NUMBER, to=to)
    print(message.sid)


def send_email(subject, msg, to="jimusbobus@hotmail.com"):
    # Create a MIMEText object to represent the email
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = SMTP_USER
    msg['To'] = to
    # to add passwords - https://myaccount.google.com/apppasswords
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SMTP_USER, password=SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_USER,
            to_addrs=to,
            msg=msg.as_string())
