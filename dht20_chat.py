import smbus2
import time

# I2Cバスを初期化 (通常Raspberry Piではバス番号は1)
bus = smbus2.SMBus(1)
DHT20_ADDR = 0x38  # DHT20センサーのI2Cアドレス

def read_dht20():
    # センサーをリセットしてデータ取得を準備するコマンド
    bus.write_i2c_block_data(DHT20_ADDR, 0xAC, [0x33, 0x00])
    time.sleep(0.1)  # 少し待機してセンサーを準備させる

    # 7バイトのデータを読み取る
    data = bus.read_i2c_block_data(DHT20_ADDR, 0x00, 7)

    # データが正しく読み込めたか確認
    if data:
        # 湿度の計算
        humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) / 1048576 * 100
        # 温度の計算
        temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) / 1048576 * 200 - 50
        return temperature, humidity
    return None, None

# センサーからデータを取得し、表示する
while True:
    temp, hum = read_dht20()
    if temp and hum:
        print(f"Temperature: {temp:.2f} °C, Humidity: {hum:.2f} %")
    else:
        print("Failed to read data from DHT20")
    time.sleep(2)
