import smbus
import time

# I2Cチャンネル (Raspberry Piでは通常1)
bus = smbus.SMBus(1)
DHT20_ADDR = 0x38  # DHT20のI2Cアドレス

def read_dht20():
    # データ取得コマンドの送信
    bus.write_byte(DHT20_ADDR, 0xAC)
    time.sleep(0.1)  # センサーが準備完了になるまで待機

    # 7バイトのデータを読み込む
    data = bus.read_i2c_block_data(DHT20_ADDR, 0x00, 7)

    if data:
        # 湿度を計算
        humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) / 1048576 * 100
        # 温度を計算
        temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) / 1048576 * 200 - 50
        return temperature, humidity
    return None, None

# ループでデータを取得
while True:
    temperature, humidity = read_dht20()
    if temperature and humidity:
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity:.2f} %")
    else:
        print("Failed to read from DHT20")
    time.sleep(2)
