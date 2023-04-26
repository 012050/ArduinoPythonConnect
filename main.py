import serial.tools.list_ports
import os
import time
import pyautogui

device = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(device):
    # print(f"port: {port}: desc: {desc} hwid: [{hwid}]")
    print(port)
    desc = desc.split()[1].split('(')[0]
    print(desc)
    print(hwid)
    if desc == "Leonardo":
        print("아두이노 연결 성공")
        port_data = port

try:
    py_serial = serial.Serial(
        # Window
        # port=f'COM{port_data}',
        port=port_data,

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
    if c_commend == '':
        c_commend = 'a'
    elif c_commend == "exit":
        print("시리얼 통신 종료")
        break
    py_serial.write(c_commend.encode())
    time.sleep(0.1)