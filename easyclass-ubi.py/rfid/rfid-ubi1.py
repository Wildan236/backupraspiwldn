import requests
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time

# Ubidots setup
UBIDOTS_TOKEN = "BBFF-R7ydNyQLvtvBFdtSwZ5sbSJnrGqnad"
VARIABLE_ID = "rfid"
UBIDOTS_URL = f"https://industrial.api.ubidots.com/api/v1.6/devices/rfid/values/"

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
    try:
        while True:
            rfid_data = read_rfid()
            send_to_ubidots(rfid_data)
            time.sleep(1)  # Mengatur interval waktu pengiriman data (10 detik dalam contoh ini)
    except KeyboardInterrupt:
        print("Pengiriman data RFID ke Ubidots dihentikan.")
    GPIO.cleanup()
