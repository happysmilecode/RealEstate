import os
import json
import smtplib
import ssl
from email.headerregistry import Address
from email.message import EmailMessage
from email_split import email_split


base_path = os.path.dirname(os.path.realpath(__file__))
sett_path = os.path.join(base_path, '..', '..', 'settings')


def load_settings():
    with open(os.path.join(sett_path, 'email.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


def prepare_email(email):
    return email_split(email).local, email_split(email).domain


def send_email(from_address, to_address, subject, plaintext, html=None):

    # Load the e-mail sending settings
    settings = load_settings()

    # Prepare sending receiver settings
    to = (
        Address(
            display_name=settings.get('display_name'),
            username=to_address['username'],
            domain=to_address['domain']
        ),
    )

    # Prepare the message
    message = EmailMessage()
    message['From'] = from_address
    message['To'] = to
    message['Subject'] = subject
    message.set_content(plaintext)

    # Add HTML formatting as an alternative
    if html is not None:
        message.add_alternative(html, subtype='html')

    # Prepare the SSL context
    ssl_context = ssl.create_default_context()

    # Prepare the host and port
    host, port = settings.get('server'), int(settings.get('port'))

    # Send the message
    with smtplib.SMTP_SSL(host=host, port=port, context=ssl_context) as smtp_server:
        smtp_server.login(settings.get('email_address'), settings.get('email_password'))
        smtp_server.send_message(message)
