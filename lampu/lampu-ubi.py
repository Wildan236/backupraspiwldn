import requests
import RPi.GPIO as GPIO
import time

# Nonaktifkan peringatan channel sudah digunakan
GPIO.setwarnings(False)

# Konfigurasi pin relay di Raspberry Pi
RELAY_PIN = 22
RELAY_PIN2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN2, GPIO.OUT)

# Ubidots API URL dan Token
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/"
TOKEN = "BBFF-2jXFcArgZADJPrXdNDezHs4Q95gudr"
DEVICE_LABEL = "lain"
VARIABLE_LABEL1 = "ac"
VARIABLE_LABEL2 = "tv"

# Fungsi untuk mengontrol lampu
def toggle_lamp(status):
    GPIO.output(RELAY_PIN, status)
    if status:
        print("ac menyala")
    else:
        print("ac mati")

def toggle_lamp2(status):
    GPIO.output(RELAY_PIN2, status)
    if status:
        print("tv menyala")
    else:
        print("tv mati")

# Fungsi untuk mendapatkan data dari Ubidots
def get_ubidots_data():
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(device_label=DEVICE_LABEL, variable_label=VARIABLE_LABEL1)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None


def get_ubidots_data2():
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(device_label=DEVICE_LABEL, variable_label=VARIABLE_LABEL2)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None


try:
    while True:
        lamp_status = get_ubidots_data()
        lamp_status2 = get_ubidots_data2()

        if lamp_status is not None:
            toggle_lamp(int(lamp_status))
        else:
            print("Data tidak lengkap atau tidak ada nilai (value) yang diterima untuk AC.")

        if lamp_status2 is not None:
            toggle_lamp2(int(lamp_status2))
        else:
            print("Data tidak lengkap atau tidak ada nilai (value) yang diterima untuk TV.")

        time.sleep(0.05)  # Perbarui status lampu setiap 1 detik
        
except KeyboardInterrupt:
    GPIO.cleanup()

