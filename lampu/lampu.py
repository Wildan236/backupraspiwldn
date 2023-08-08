import RPi.GPIO as GPIO
import time

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# Fungsi untuk menyalakan lampu
def turn_on():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)

# Fungsi untuk mematikan lampu
def turn_off():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
try:
    while True:
        # Panggil fungsi untuk menyalakan lampu
        turn_on()
        time.sleep(0.05)  # Tunggu selama 1 detik

        # Panggil fungsi untuk mematikan lampu
        turn_off()
        time.sleep(0.05)  # Tunggu selama 1 detik

except KeyboardInterrupt:
    # Hentikan program jika pengguna menekan Ctrl+C
    GPIO.cleanup()
