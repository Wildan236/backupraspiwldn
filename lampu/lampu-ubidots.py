import requests
import RPi.GPIO as GPIO
import time

# Konfigurasi pin relay di Raspberry Pi
RELAY_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Ubidots API URL dan Token
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/"
TOKEN = "BBFF-2jXFcArgZADJPrXdNDezHs4Q95gudr"
DEVICE_LABEL = "lain"
VARIABLE_LABEL = "ac b"

# Fungsi untuk mengontrol lampu
def toggle_lamp(status):
     GPIO.output(RELAY_PIN, status)

# Fungsi untuk mendapatkan data dari Ubidots
def get_ubidots_data():
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(device_label=DEVICE_LABEL, variable_label=VARIABLE_LABEL)
    response = requests.get(url, headers=headers)
    data = response.json()
    value = data["last_value"]["value"]
    return value

try:
    while True:
        lamp_status = get_ubidots_data()
        toggle_lamp(int(lamp_status))
        time.sleep(1)  # Perbarui status lampu setiap 5 detik
        
except KeyboardInterrupt:
    GPIO.cleanup()
