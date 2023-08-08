import requests
import RPi.GPIO as GPIO
import time

# Pengaturan pin GPIO
GPIO.setmode(GPIO.BCM)
relay_pin = 22
GPIO.setup(relay_pin, GPIO.OUT)

# API token dari Ubidots
api_token = 'BBFF-R7ydNyQLvtvBFdtSwZ5sbSJnrGqnad'

# URL endpoint untuk mengakses variabel di Ubidots
base_url = 'http://industrial.api.ubidots.com/api/v1.6/devices/'
device_label = 'Demo'
variable_label = 'tombol'
url = f'{base_url}{device_label}/{variable_label}'

# Fungsi untuk mengaktifkan relay
def turn_relay_on():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Relay turned OFF")

# Fungsi untuk mematikan relay
def turn_relay_off():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Relay turned ON")
    print("==================")

try:
    while True:
        # Mengambil data dari Ubidots
        headers = {'X-Auth-Token': api_token}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            value = data['last_value']['value']
            
            # Memeriksa apakah relay harus diaktifkan atau dimatikan berdasarkan nilai variabel dari Ubidots
            if value == 0:
                turn_relay_on()
            elif value == 1:
                turn_relay_off()
            else:
                print("Nilai variabel tidak valid")
        
        else:
            print("Gagal mendapatkan data dari Ubidots. Status code:", response.status_code)

        # Tunggu sejenak sebelum memperbarui status relay
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Program dihentikan melalui keyboard interrupt")
finally:
    # Memastikan pin GPIO diatur ke nilai awal dan membersihkan GPIO
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()

