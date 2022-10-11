import smtplib
from email.mime.text import MIMEText

from django.conf import settings
from myPortafolio.wsgi import *
from django.test import TestCase

# Create your tests here.
def send_email():
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to='yandivd@gmail.com'

        #construir el mensaje
        mensaje= MIMEText("""Alguien ha dejado un testimonio acerca de ti""")
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = 'Testimonio en myPortafolio'

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)

send_email()
