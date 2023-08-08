import time
import RPi.GPIO as GPIO
from ubidots import ApiClient

# Konfigurasi pin Relay pada Raspberry Pi
relay_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Konfigurasi API Ubidots
api = ApiClient("BBFF-R7ydNyQLvtvBFdtSwZ5sbSJnrGqnad")  # Ganti dengan API key Anda

# Ubah "YOUR_DEVICE_LABEL" dan "YOUR_VARIABLE_LABEL" dengan label Device dan Variable yang sudah dibuat di Ubidots
device = api.get_device("Demo")
variable = device.get_variable("tombol")

def turn_on_relay():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Relay turned ON")
    variable.save_value(1)  # Kirim nilai 1 ke Ubidots

def turn_off_relay():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Relay turned OFF")
    variable.save_value(0)  # Kirim nilai 0 ke Ubidots

if __name__ == "__main__":
    try:
        while True:
            # Contoh penggunaan: Hidupkan Relay selama 5 detik, kemudian matikan selama 5 detik.
            turn_on_relay()
            time.sleep(1)
            turn_off_relay()
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
