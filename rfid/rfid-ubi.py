import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Ubidots setup
UBIDOTS_TOKEN = "BBFF-R7ydNyQLvtvBFdtSwZ5sbSJnrGqnad"
VARIABLE_ID = "rfid"
UBIDOTS_URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/rfid"

def read_rfid():
    reader = SimpleMFRC522()
    try:
        print("Tempelkan kartu RFID...")
        id, text = reader.read()
        print(f"Kartu terbaca: ID={id}, Data={text}")
        return text.strip()
    finally:
        GPIO.cleanup()

def send_to_ubidots(data):
    headers = {
        "X-Auth-Token": UBIDOTS_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        VARIABLE_ID: data
    }
    response = requests.post(UBIDOTS_URL, headers=headers, json=payload)
    print("Data berhasil dikirim ke Ubidots.")
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    while True:
        rfid_data = read_rfid()
        send_to_ubidots(rfid_data)
