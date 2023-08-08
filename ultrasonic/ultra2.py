import RPi.GPIO as GPIO
import time

# Deklarasi pin trigger dan echo pada Raspberry Pi
trigger_pin = 23
echo_pin = 24

def setup():
    # Mengatur mode pin pada Raspberry Pi
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def get_distance():
    # Mengirimkan sinyal trigger selama 10 mikrodetik
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    # Membaca durasi pulsa echo
    start_time = time.time()
    end_time = time.time()
    while GPIO.input(echo_pin) == GPIO.LOW:
        start_time = time.time()
    while GPIO.input(echo_pin) == GPIO.HIGH:
        end_time = time.time()

    # Menghitung jarak berdasarkan durasi
    duration = end_time - start_time
    distance = duration * 34300 / 2  # Kecepatan suara adalah 343 m/s
    print("distance")
    return distance

def cleanup():
    # Membersihkan pin GPIO pada Raspberry Pi
    GPIO.cleanup()

# Pemanggilan fungsi setup() sebelum penggunaan sensor
setup()
distance = get_distance()

        # Menampilkan hasil jarak
print("Jarak: %.2f cm" % distance)

time.sleep(0.5)  # Memberi jeda sebelum membaca data berikutnya

cleanup()

'''try:
    while True:
        # Membaca jarak dari sensor ultrasonik
        distance = get_distance()

        # Menampilkan hasil jarak
        print("Jarak: %.2f cm" % distance)

        time.sleep(0.5)  # Memberi jeda sebelum membaca data berikutnya

except KeyboardInterrupt:
    # Memberhentikan program dengan menekan Ctrl + C
    cleanup()'''