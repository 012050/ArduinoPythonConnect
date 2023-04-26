import serial
import time
import os
import pyautogui

# port.txt 파일에 저장된 포트 번호를 읽어옴
try:
    f = open(os.getcwd() + "\port.txt")
    port_data = f.read()
    f.close()
except:
    print("port.txt 파일이 없습니다.")
    pyautogui.alert("port.txt 파일이 없습니다.")
    port_data = input("포트 번호를 입력해 주세요: ")
    f = open(os.getcwd() + "\port.txt", 'w')
    f.write(port_data)
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
    if py_serial.readable():
        response = py_serial.readline()
        a_command = str(response[:len(response)-2].decode())

        print(a_command)
    
    c_commend = input('아두이노에게 내릴 명령:')
    if c_commend == "exit":
        print("시리얼 통신 종료")
        break
    py_serial.write(c_commend.encode())
    time.sleep(0.1)