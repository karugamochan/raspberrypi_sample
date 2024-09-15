import time                          # 必要なライブラリーのインポート
import board
import busio
import adafruit_ahtx0

i2c = busio.I2C(board.GP1,board.GP0)                    # I2Cバスの準備
sensor = adafruit_ahtx0.AHTx0(i2c)   # センサーオブジェクトを作成

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)     #温度を表示
    print("Humidity: %0.1f %%" % sensor.relative_humidity)   #湿度を表示　
    time.sleep(2)