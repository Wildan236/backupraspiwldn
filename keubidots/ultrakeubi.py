import RPi.GPIO as GPIO
import time
import requests

# Konfigurasi pin GPIO
GPIO.setmode(GPIO.BOARD)
TRIG = 13
ECHO = 11

# Konfigurasi Ubidots
TOKEN = 'YOUR_UBIDOTS_TOKEN'
DEVICE_LABEL = 'YOUR_DEVICE_LABEL'
VARIABLE_LABEL = 'YOUR_VARIABLE_LABEL'

def setup():
    # Set pin TRIG sebagai output dan pin ECHO sebagai input
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Mengirimkan sinyal ultrasonik untuk mendapatkan jarak
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

def send_to_ubidots(value):
    # Mengirimkan nilai jarak ke Ubidots menggunakan API
    url = f'https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}/{VARIABLE_LABEL}/values'
    headers = {'X-Auth-Token': TOKEN, 'Content-Type': 'application/json'}
    payload = {'value': value}

    try:
        response = requests.post(url, headers=headers, json=payload)
        print('Data sent to Ubidots:', response.json())
    except requests.exceptions.RequestException as e:
        print('Failed to send data to Ubidots:', e)

def loop():
    while True:
        distance = get_distance()
        print('Distance:', distance, 'cm')
        send_to_ubidots(distance)
        time.sleep(1)

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        cleanup()


    # Menunggu hingga pin echo menjadi LOW
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Menghitung durasi pulsa
    pulse_duration = pulse_end - pulse_start

    # Menghitung jarak berdasarkan kecepatan suara
    speed_of_sound = 34300  # Kecepatan suara dalam cm/s
    distance = pulse_duration * speed_of_sound / 2

    return distance

try:
    while True:
        # Mengukur jarak
        distance = measure_distance()

        # Menampilkan hasil
        print("Jarak: %.2f cm" % distance)

        # Membuat payload data
        payload = {
            "value": distance
        }

        # Mengirim data ke Ubidots
        headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
        response = requests.post(url, headers=headers, json=payload)

        # Memeriksa status respon
        if response.status_code == 201:
            print("Data berhasil dikirim ke Ubidots")
        else:
            print("Terjadi kesalahan saat mengirim data ke Ubidots")

        # Delay sebelum pengukuran berikutnya
        time.sleep(0.1)

except KeyboardInterrupt:
    # Mematikan GPIO
    GPIO.cleanup()