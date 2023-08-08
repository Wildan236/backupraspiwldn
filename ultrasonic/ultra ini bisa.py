import RPi.GPIO as GPIO
import time

# Mengatur mode GPIO
GPIO.setmode(GPIO.BOARD)

# Menentukan pin untuk Trig dan Echo
TRIG = 11
ECHO = 13

# Mengatur pin sebagai input atau output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Mengirim sinyal trigger selama 10 mikrodetik
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Mencatat waktu mulai dan berhenti
    pulse_start = time.time()
    pulse_end = time.time()

    # Menunggu pin echo menjadi HIGH
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Menunggu pin echo menjadi LOW
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Menghitung durasi pulsa
    pulse_duration = pulse_end - pulse_start

    # Menghitung jarak (kecepatan suara adalah 34300 cm/s)
    distance = pulse_duration * 17150

    # Membulatkan jarak menjadi 2 angka desimal
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = measure_distance()
        print("Jarak: {} cm".format(dist))
        time.sleep(1)

except KeyboardInterrupt:
    # Menghentikan program dan membersihkan pin GPIO
    GPIO.cleanup()
