from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Simple Mail Transferem Protocol
import smtplib

sender = 'seu_email'
password = 'gkwl xltw uyvl xrfu'
recipient = 'email_destinatario'

# config smtp
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user_name = sender
smpt_password = 'gkwl xltw uyvl xrfu'

text = 'Olá, tudo bem?'

mime = MIMEMultipart()
mime['from'] = sender
mime['to'] = recipient
mime['subject'] = 'assunto'
message = MIMEText(text)
mime.attach(message)

with smtplib.SMTP(smtp_server,smtp_port) as s:
    s.helo()
    s.starttls()
    s.login(smtp_user_name,smpt_password)
    s.send_message(mime)
    print('Enviado!')
