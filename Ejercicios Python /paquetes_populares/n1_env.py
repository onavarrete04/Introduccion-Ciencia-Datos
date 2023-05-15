# Variables de entorno

# SENGRID_API_KEY = "FAKDHFKHASDFJHDKAFHA"

import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

apikey = os.environ.get("SENGRID_API_KEY")
email = os.environ.get("SENGRID_EMAIL")

mensaje = Mail(
    from_email=email,
    to_emails=email,
    subject="Correo de Prueba",
    html_content="Curso de <b> Ultimate Python </b>"
)

try:
    apikey = os.environ.get("SENGRID_API_KEY")
    sg = SendGridAPIClient(apikey)
    respuesta = sg.send(mensaje)
    print(
        respuesta.status_code,
        respuesta.body,
        respuesta.headers,
    )
except Exception as e:
    print(e)
