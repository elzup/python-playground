import serial


def read_from_serial(port='/dev/ttyUSB0', baudrate=9600):
    # シリアルポートを開く
    with serial.Serial(port, baudrate) as ser:
        while True:
            line = ser.readline().decode('utf-8').strip()  # 1行読み取り
            print(line)


if __name__ == '__main__':
    read_from_serial()
