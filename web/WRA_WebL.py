'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-12 11:28:22
LastEditors: 狐日泽
LastEditTime: 2023-12-15 11:32:07
'''
# import json
import asyncio
import datetime
import webbrowser
from toast import toast
from nicegui import ui, app

# def save_config(name, save_value):
#     with open(".nicegui/storage_general.json", "r", encoding="utf-8") as f:
#         config = json.load(f)
#     config[name] = save_value
#     with open(".nicegui/storage_general.json", "w", encoding="utf-8") as f:
#         json.dump(config, f, ensure_ascii=False)

async def wra():
    try:
        TimeLeft = (TextHours.value * 3600) + (TextMinutes.value * 60) + TextSeconds.value
    except TypeError:
        ui.notify("倒计时不该为空！")
        return
    start_button.disable()
    cancel_button.enable()
    badge.set_text(int(TimeLeft))
    badge.set_visibility(True)
    TextTimeLeft.set_text("")
    while int(TimeLeft) > 0:
        print(TimeLeft) # debug
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            raise
        TimeLeft = int(TimeLeft) - 1
        badge.set_text(int(TimeLeft))
    else:
        if voice_switch:
            voice.play()
            voice_button.enable()
        TextTimeLeft.set_text("上次提醒时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        app.storage.general['time_left_count'] = app.storage.general.get('time_left_count', 0) + 1
        start_button.enable()
        cancel_button.disable()
        badge.set_visibility(False)
        await toast(Title.value, Launch.value, scenario=toggle_scenario.value, duration=toggle_duration.value)

def voice_pause():
    voice.pause()
    voice_button.disable()

def reset_config():
    TextHours.set_value(0)
    TextMinutes.set_value(0)
    TextSeconds.set_value(0)
    color_choose.set_value('#D7EEFF')
    toggle_duration.set_value('short')
    toggle_scenario.set_value('reminder')
    voice_switch.set_value(False)
    voice_src.set_value('https://cdn.pixabay.com/download/audio/2022/10/14/audio_9939f792cb.mp3')

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
        badge.set_visibility(False)

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
    global badge
    global voice_switch
    global voice_button
    global voice_src
    global voice
    global color_choose

    ui.badge('WRA For Web Local | WRA-WebL v1.1.0', text_color='#ffeded')
    with ui.row():
        with ui.badge('计时次数', outline=True):
            ui.badge('0',outline=True).bind_text_from(app.storage.general, 'time_left_count')
        ui.button('恢复默认设置', on_click=lambda: reset_config())

    color_choose = ui.color_input(label="背景色", on_change=lambda e: ui.query('body').style(f'background-color: {e.value}'), value="#D7EEFF").bind_value(app.storage.general, 'bg_color')
    ui.query('body').style(f'background-color: {color_choose.value}')

    with ui.row():
        TextHours = ui.number(label="时", value=0, format="%.0f").bind_value(app.storage.general, 'TimeHours')
        TextMinutes = ui.number(label="分", value=0, format="%.0f").bind_value(app.storage.general, 'TimeMinutes')
        TextSeconds = ui.number(label="秒", value=0, format="%.0f").bind_value(app.storage.general, 'TimeSeconds')

    with ui.row():
        Title = ui.input(label="通知标题")
        Launch = ui.input(label="通知内容")

    with ui.row():
        ui.label("通知场景")
        toggle_scenario = ui.toggle(["reminder", "alarm", "incomingCall", "urgent"], value="reminder").bind_value(app.storage.general, 'scenario')

    with ui.row():
        ui.label("留存时间")
        toggle_duration = ui.toggle(["long", "short"], value="short").bind_value(app.storage.general, 'duration')

    with ui.row():
        with ui.button('开始计时', on_click=lambda: start_task()) as start_button:
            badge = ui.badge('', color='green').props('floating')
            badge.set_visibility(False)
        cancel_button = ui.button('取消计时', on_click=lambda: cancel_task())
        cancel_button.disable()
        ui.button('浏览器访问', on_click=lambda: webbrowser.open_new_tab(f"http://127.0.0.1:{port}"))
        voice_switch = ui.switch('通知声音', value=False).bind_value(app.storage.general, 'vioce_switch')
    with ui.row():
        voice_button = ui.button("暂停播放", on_click=lambda: voice_pause()).bind_visibility_from(voice_switch, 'value')
        voice_button.disable()
        voice_src = ui.input(label='通知声音(重启生效)', value='https://cdn.pixabay.com/download/audio/2022/10/14/audio_9939f792cb.mp3').bind_visibility_from(voice_switch, 'value').bind_value(app.storage.general, 'voice_src')
        voice = ui.audio(voice_src.value, controls=False)

    TextTimeLeft = ui.label()

    with ui.footer(value=False) as footer:
        ui.markdown("CopyRight © 2023 [SageSoft](https://sagesoft.ltd) & [Nya-WSL](https://nya-wsl.com) Powered by [NiceGUI](https://nicegui.io)")
    with ui.page_sticky(position='bottom-right', x_offset=10, y_offset=10):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

port = 3333
ui.run(port=port, favicon="⏰", title="WRA-WebL", native=True, frameless=False, window_size=[600, 610], reload=False, show=True, storage_secret='SageSoft', language="zh-CN")