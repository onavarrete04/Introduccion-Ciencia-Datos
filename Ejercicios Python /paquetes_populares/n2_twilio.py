import os
from twilio.rest import Client

try:
    sid = os.environ.get("TWILIO_SID")
    token = os.environ.get("TWILIO_TOKEN")
    numero = os.environ.get("TWILIO_N")

    cliente = Client(sid, token)

    mensaje = cliente.messages.create(
        body="Hola ALE avisame si te llego este mensaje, atentamente Oscar",
        from_=numero,
        to="+13014715523"

    )
except Exception as e:
    print(e)
