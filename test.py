import serial, time

def check_arduino():
    PORT = '/dev/ttyUSB0'   # подставьте ваш порт
    ser = serial.Serial(PORT, 9600, timeout=1)
    time.sleep(2)           # ждём перезагрузку Arduino

    line = ser.readline()
    ser.close()

    return line


print(check_arduino())