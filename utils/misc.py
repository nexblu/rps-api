from email.message import EmailMessage
import ssl
import smtplib
import os
import requests


class Misc:
    @staticmethod
    def cek_inputan(email, nama, pesan):
        input_kosong = []

        if email == '':
            input_kosong.append('email')
        if nama == '':
            input_kosong.append('name')
        if pesan == '':
            input_kosong.append('message')

        return input_kosong

    @staticmethod
    def get_array_item_by_value(arr, target_value):
        try:
            index = arr.index(target_value)
            return arr[index]
        except ValueError:
            return None

    @staticmethod
    def check_email(email: str):
        url = 'https://community-neutrino-email-validate.p.rapidapi.com/email-validate'

        payload = {
            'email': email,
            'fix-typos': 'false'
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'X-RapidAPI-Key': '24ed65ae48msha241654d8bc9256p17cb04jsn525ebae94435',
            'X-RapidAPI-Host': 'community-neutrino-email-validate.p.rapidapi.com'
        }

        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            resp = response.json()
            return resp
        else:
            return None

    @staticmethod
    def send_email(email: str, name: str, content: str):
        email_sender = os.environ.get('EMAIL_SENDER')
        email_password = os.environ.get('EMAIL_PASSWORD')
        email_receiver = os.environ.get('EMAIL_RECEIVER')
        email_host = os.environ.get('SMTP_HOST')
        email_port = os.environ.get('SMTP_PORT')

        subject = f'{email} ({name})'

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(content)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(email_host, email_port, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
