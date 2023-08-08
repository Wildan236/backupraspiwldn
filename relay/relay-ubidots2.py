import requests
import time

# Konfigurasi Ubidots
UBIDOTS_TOKEN = "BBFF-R7ydNyQLvtvBFdtSwZ5sbSJnrGqnad"
DEVICE_LABEL = "Demo"

# URL untuk mengirim data ke Ubidots
BASE_URL = "https://industrial.ubidots.com/app/devices/64a53dbdb9e4ca001057b663/64c71baac06e0d08c8ab1409"
POST_URL = BASE_URL + "https://industrial.ubidots.com/app/devices/64a53dbdb9e4ca001057b663/64c71baac06e0d08c8ab1409".format(label=DEVICE_LABEL, token=UBIDOTS_TOKEN)

# Fungsi untuk mengontrol relay dan mengirim statusnya ke Ubidots
def control_relay(relay_status):
    # Simpan data relay_status ke Ubidots
    payload = {"relay": relay_status}
    try:
        response = requests.post(POST_URL, json=payload)
        if response.status_code == 201:
            print("Data successfully sent to Ubidots.")
        else:
            print("Failed to send data. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Main program
if __name__ == "__main__":
    try:
        while True:
            # Contoh pengontrolan relay berdasarkan kondisi tertentu
            # Anda bisa menyesuaikan kode ini sesuai kebutuhan Anda.
            
            # Misalnya, jika suhu di Raspberry Pi melebihi ambang batas tertentu, hidupkan relay.
            temperature = 25  # Ganti nilai ini dengan membaca suhu dari sensor suhu yang sesuai di Raspberry Pi.
            threshold_temperature = 30

            if temperature > threshold_temperature:
                control_relay(1)  # Hidupkan relay
            else:
                control_relay(0)  # Matikan relay

            time.sleep(5)  # Jeda selama 5 detik sebelum membaca suhu lagi
    except KeyboardInterrupt:
        print("Program berhenti oleh pengguna.")
