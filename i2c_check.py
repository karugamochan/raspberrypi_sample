import smbus2
import time

bus = smbus2.SMBus(1)  # バス番号1を指定
DHT20_ADDR = 0x38  # デバイスアドレスが正しいことを確認

try:
    # デバイスへのコマンド送信
    bus.write_i2c_block_data(DHT20_ADDR, 0xAC, [0x33, 0x00])
    time.sleep(0.1)
    # データ取得
    data = bus.read_i2c_block_data(DHT20_ADDR, 0x00, 7)
    print(f"Received data: {data}")
except IOError as e:
    print(f"I2C communication error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    bus.close()  # バスを閉じる