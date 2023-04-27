import serial.tools.list_ports
import os
import time
import pyautogui

board_name = "Nano"
try:
    device = serial.tools.list_ports.comports()

    print(device[0][1])
    print(device[1])
    print(len(device))

    print("연결된 보드 확인\n---------------------------------------------------------------")
    for port_list, desc, hwid in sorted(device):
        print(port_list)
        desc = desc.split()[1].split('(')[0]
        print(desc)
        print(hwid)
        print("---------------------------------------------------------------")
        # 보드 이름
        if desc == board_name:
            port_data = port_list
    # if device[len(device)-1]:
    #     print("{} 보드가 없습니다.\n{} : {} 보드에 연결을 시도합니다.".format(board_name, port_list, desc))
    #     port_data = port_list
    #     board_name = desc
except:
    print("연결된 보드가 없습니다.")
    pyautogui.alert("연결된 보드가 없습니다.", "Error")
    exit()
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
    pyautogui.alert("아두이노 {}의 연결을 확인해 주세요.".format(board_name), "Error")
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