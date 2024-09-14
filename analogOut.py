import gpiozero
import time

pin = gpiozero.PWMOutputDevice(pin=17, frequency=1000)
try:
    while True:
        values = [0.0, 0.1, 0.5, 1.0, 0.5, 0.1]
        for value in values:
            pin.value = value
            time.sleep(1)
finally:
    pin.close()