import time
import RPi.GPIO as GPIO
from ubidots import ApiClient

GPIO.setmode(GPIO.BOARD)
trigger_pin = 13
echo_pin = 11
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

api = ApiClient(token='a88d181b90a79a2b9c708fa9a1c88b4a29b')

def measure_distance():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def measure_distance():
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

while True:
    distance=measure_distance()
    print("Distance: {} cm".format(distance))

    # Kirim data ke Ubidots
    variable = api.get_variable('VARIABLE_ID')
    response = variable.save_value({'value': distance})

    time.sleep(1)  # Tunggu 1 detik sebelum mengukur kembali



