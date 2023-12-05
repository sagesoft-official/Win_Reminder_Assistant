'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-04 00:01:16
LastEditors: 狐日泽
LastEditTime: 2023-12-06 02:03:08
'''

import sys
import time
import datetime
import PySimpleGUI as sg
from win11toast import toast

version = "1.2.1"

layout = [[sg.Text("时（必须为>=1的整数，留空默认为0）")],
        [sg.Input(key='-TimeHours-')],
        [sg.Text("分（必须为>=1的整数，留空默认为0）")],
        [sg.Input(key='-TimeMinutes-')],
        [sg.Text("秒（必须为>=0的整数，留空默认为0）")],
        [sg.Input(key='-TimeSeconds-')],
        [sg.Text("通知标题")],
        [sg.Input(key='-title-')],
        [sg.Text("通知内容")],
        [sg.Input(key='-launch-')],
        [sg.Text("通知场景")],
        [sg.Text("reminder[默认]，alarm[无效]，incomingCall，urgent")],
        [sg.Input(key='-scenario-')],
        [sg.Text("通知时间（long，short，默认short）")],
        [sg.Input(key='-duration-')],
        [sg.Text("", size=(40,1), key='-OUTPUT-')],
        [sg.Button('确定')]]

window = sg.Window(f'Windows提醒小助手v{version}', layout=layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    TimeLeft = 0
    if values['-TimeHours-'] == "" and values['-TimeMinutes-'] == "" and values['-TimeSeconds-'] == "":
        ErrorPopup = sg.popup("倒计时不该为空！")
        if ErrorPopup == None or ErrorPopup == "OK":
            pass
    else:
        if values['-TimeHours-'] == "":
            values['-TimeHours-'] = 0
        if values['-TimeMinutes-'] == "":
            values['-TimeMinutes-'] = 0
        if values['-TimeSeconds-'] == "":
            values['-TimeSeconds-'] = 0

        TimeLeft = (int(values['-TimeHours-']) * 3600) + (int(values['-TimeMinutes-']) * 60) + int(values['-TimeSeconds-'])
        StartTimeLeft = sg.popup_yes_no(f"单击Yes开始计时，单击No取消计时，预计时间：{TimeLeft}秒", title="是否开始倒计时？")
        if StartTimeLeft == None or StartTimeLeft == "No":
            pass
        else:
            if values['-scenario-'] == "":
                values['-scenario-'] = 'reminder'
            if values['-duration-'] == "":
                values['-duration-'] = 'short'

            while int(TimeLeft) > 0:
                if event == sg.WINDOW_CLOSED or event == 'Quit':
                    sys.exit()
                window.refresh()
                print(TimeLeft) # debug
                time.sleep(1)
                TimeLeft = int(TimeLeft) - 1
                window.refresh()
                window['-OUTPUT-'].update(f"倒计时：{TimeLeft}")
            else:
                toast(values['-title-'], values['-launch-'], scenario=values['-scenario-'], duration=values['-duration-'])
                window['-OUTPUT-'].update(f"上次提醒时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

window.close()