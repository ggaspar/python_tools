import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE

def send_mail(msg):
    EMAIL_SOURCE = "toto@gmail.com"
    EMAIL_DESTINATIONS = ["xoxo@gmail.com","zozo@gmail.com"]
    EMAIL_SERVER = "mail2.company.com"

    subject = "Subject"
    text = "***THIS IS AN AUTOMATIC MESSAGE*** \n" + msg

    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = EMAIL_SOURCE
    msg['To'] = COMMASPACE.join(EMAIL_DESTINATIONS)
    msg.attach(MIMEText(text))

    smtp = smtplib.SMTP(EMAIL_SERVER)
    smtp.sendmail(EMAIL_SOURCE, EMAIL_DESTINATIONS, msg.as_string())
    smtp.close()