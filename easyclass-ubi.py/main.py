from module.rfid_module import *
import time
time.sleep(2)





tulis_rfid(name="NAUFI")
id, text=baca_rfid()
print(text)

GPIO.cleanup()