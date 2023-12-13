'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-12 11:28:22
LastEditors: 狐日泽
LastEditTime: 2023-12-13 13:45:47
'''
import json
import asyncio
import datetime
from nicegui import ui, app
from toast import toast

def save_config(name, save_value):
    with open(".nicegui/storage_general.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    config[name] = save_value
    with open(".nicegui/storage_general.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False)

async def wra():
    try:
        TimeLeft = (TextHours.value * 3600) + (TextMinutes.value * 60) + TextSeconds.value
    except TypeError:
        ui.notify("倒计时不该为空！")
        return
    start_button.disable()
    cancel_button.enable()
    while int(TimeLeft) > 0:
        print(TimeLeft) # debug
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            raise
        TimeLeft = int(TimeLeft) - 1
        TextTimeLeft.set_text("倒计时：" + str(TimeLeft))
    else:
        TextTimeLeft.set_text("上次提醒时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        app.storage.general['time_left_count'] = app.storage.general.get('time_left_count', 0) + 1
        await toast(Title.value, Launch.value, scenario=toggle_scenario.value, duration=toggle_duration.value)

def start_task():
    global task
    task = asyncio.create_task(wra())

async def cancel_task():
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        ui.notify("计时已取消")
        start_button.enable()
        cancel_button.disable()

@ui.page('/')
def index():
    global TextHours
    global TextMinutes
    global TextSeconds
    global Title
    global Launch
    global toggle_scenario
    global toggle_duration
    global TextTimeLeft
    global start_button
    global cancel_button
    app.storage.general["bg_color"] = app.storage.general.get('bg_color')
    if app.storage.general["bg_color"] == "":
        app.storage.general["bg_color"] = "#D7EEFF"

    ui.label('WRA For Web Local | WRA-WebL v1.0.1')
    with ui.row():
       ui.label('累计计时次数:')
       ui.label().bind_text_from(app.storage.general, 'time_left_count')
    ui.link(f'浏览器访问', f'http://127.0.0.1:{port}', new_tab=True)
    ui.color_input(label="背景色", on_change=lambda e: ui.query('body').style(f'background-color: {e.value}'), value="#D7EEFF").bind_value_to(app.storage.general, 'bg_color')
    ui.query('body').style(f'background-color: {app.storage.general["bg_color"]}')

    with ui.row():
        TextHours = ui.number(label="时", value=0, format="%.0f").bind_value(app.storage.general, 'TimeHours')
        TextMinutes = ui.number(label="分", value=0, format="%.0f").bind_value(app.storage.general, 'TimeMinutes')
        TextSeconds = ui.number(label="秒", value=0, format="%.0f").bind_value(app.storage.general, 'TimeSeconds')

    Title = ui.input(label="通知标题", on_change=lambda e: save_config("title", e.value))
    Launch = ui.input(label="通知内容", on_change=lambda e: save_config("launch", e.value))

    ui.label("通知场景")
    toggle_scenario = ui.toggle(["reminder", "alarm", "incomingCall", "urgent"], value="reminder").bind_value(app.storage.general, 'scenario')

    ui.label("通知留存时间")
    toggle_duration = ui.toggle(["long", "short"], value="short").bind_value(app.storage.general, 'duration')

    with ui.row():
        start_button = ui.button('开始计时', on_click=lambda: start_task())
        cancel_button = ui.button('取消计时', on_click=lambda: cancel_task())
        cancel_button.disable()

    TextTimeLeft = ui.label()

port = 3333
ui.run(port=port, favicon="⏰", title="WRA-WebL", native=True, frameless=False, window_size=[800, 760], reload=False, show=True, storage_secret='SageSoft')