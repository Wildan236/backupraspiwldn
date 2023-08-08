import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

try:
        print("Hold tag near the module...")
        rfid.write("Wildans")
        print("Written")
finally:
        GPIO.cleanup()

# try overwrite id


