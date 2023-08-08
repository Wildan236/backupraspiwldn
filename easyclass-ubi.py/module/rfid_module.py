import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()


def tulis_rfid(name):
    print("Hold tag near the module...")
    rfid.write(name)
    print(f"Written {name}")   

def baca_rfid():
    id, text = rfid.read()
    print(id)
    print(text)
    return id, text
