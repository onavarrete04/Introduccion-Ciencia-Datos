"""PROTOCOLO SMTP"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# Solo sirve con ese protocolo, pero gmail lo considera inseguro


mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "abc04@gmail.com"

mensaje["subject"] = "Esto es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # nos identifica con el servicor y el dominio para enviar correos
    smtp.starttls()  # transporte layer security

    smtp.login("abs04@gmail.com", "Pafd")
    smtp.send_message(mensaje)

# Esto da error porque hay doble autenticación y toca habilitar otras opciones de contraseña que en el momento no tengo disponible
