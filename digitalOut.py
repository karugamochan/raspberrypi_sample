import gpiozero
import time

pin = gpiozero.DigitalOutputDevice(pin=17)
try:
    while True:
        pin.on()
        time.sleep(0.2)
        pin.off()
        time.sleep(0.8)
finally:
    pin.close()