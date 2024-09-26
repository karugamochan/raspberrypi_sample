import time
import board
import busio
import adafruit_ahtx0

# I2C
i2c = busio.I2C(board.SCL,board.SDA)
#dht20 = adafruit_dht.DHT20(board.I2C())
sensor = adafruit_ahtx0.AHTx0(i2c)
while True:
    try:
        # 
        temperature = sensor.temperature
        humidity = sensor.relative_humidity

        print(f"Temperature: {temperature:.2f} C")
        print(f"Humidity: {humidity:.2f} %")

    except RuntimeError as error:
        # 
        print(f"Error reading data: {error}")

    time.sleep(2)  # 2
