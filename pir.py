import gpiozero
import time

pin = gpiozero.DigitalInputDevice(pin=17)
try:
    while True:
    	if pin.value==1:
    		print("human exist")
    	else:
	        print("human not exist")
        time.sleep(1)
finally:
    pin.close()