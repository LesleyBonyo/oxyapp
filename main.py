import serial
ser = serial.Serial("com3",115200)
bloodlevel = ser.read(5).decode('utf-8')
heartrate = ser.read(5).decode('utf-8')