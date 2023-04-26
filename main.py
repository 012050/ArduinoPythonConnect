import serial
import time
import os
import pyautogui

# port.txt 파일에 저장된 포트 번호를 읽어옴
f = open(os.getcwd() + "\port.txt")
port_data = f.read()
f.close()

try:
    py_serial = serial.Serial(
        # Window
        port=f'COM{port_data}',

        # Linux
        # port=f'/dev/ttyACM{port_data}',

        # 보드 레이트 (통신 속도)
        baudrate=9600,
    )
except:
    print("아두이노 연결 오류")
    pyautogui.alert("아두이노 연결을 확인해 주세요.")
    exit()

while True:
    time.sleep(0.1)
    if py_serial.readable():
        response = py_serial.readline()
        command = str(response[:len(response)-2].decode())
        if command == "connected":
            print("Arduino connected...System start")
            continue
        else:
            print(command)