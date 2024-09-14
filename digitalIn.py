import gpiozero
import time

pin = gpiozero.DigitalInputDevice(pin=27, pull_up=True)
try:
    while True:
        print(pin.value)
        time.sleep(1)
finally:
    pin.close()