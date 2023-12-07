'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-06 21:56:21
LastEditors: 狐日泽
LastEditTime: 2023-12-07 10:17:10
'''
import time
from win11toast import toast
import tkinter.messagebox as tkmb
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)

def relative_to_assets(path: str):
    return "assets/frame0/" + path

def wra():
    TimeLeft = 0
    TimeHours = entry_1.get()
    TimeMinutes = entry_2.get()
    TimeSeconds = entry_3.get()
    Launch = entry_4.get()
    scenario = entry_5.get()
    duration = entry_6.get()
    Title = entry_7.get()

    if TimeHours == "" and TimeMinutes == "" and TimeSeconds == "":
        TimeError = tkmb.showerror(title="参数错误", message="倒计时不该为空！")
        if TimeError:
            return
    if TimeHours == "":
        TimeHours = 0
    if TimeMinutes == "":
        TimeMinutes = 0
    if TimeSeconds == "":
        TimeSeconds = 0
    if scenario == "":
        scenario = 'reminder'
    if duration == "":
        duration = 'short'
    TimeLeft = (int(TimeHours) * 3600) + (int(TimeMinutes) * 60) + int(TimeSeconds)
    StartTimeLeft = tkmb.askyesno(
            "SageSoft | Nya-WSL",
            "单击Yes开始计时，单击No取消计时\n"
            f"预计时间：{TimeLeft}秒")
    if not StartTimeLeft:
        return
    while int(TimeLeft) > 0:
        print(TimeLeft) # debug
        time.sleep(1)
        TimeLeft = int(TimeLeft) - 1
        LeftText = canvas.create_text(
            175.0,
            273.0,
            anchor="nw",
            text=f"倒计时：{TimeLeft}",
            fill="#000000",
            font=("Inter", 12 * -1)
            )
        window.update()
        canvas.delete(LeftText)
    else:
        global LastTimeText
        toast(Title, Launch, scenario=scenario, duration=duration)


version = "1.3.0"
window = Tk()
window.iconbitmap("icon.ico")
window.title(f"Windows提醒小助手v{version} By. SageSoft")
window.geometry("400x350")
window.configure(bg = "#D6EEFF")

canvas = Canvas(
    window,
    bg = "#D6EEFF",
    height = 350,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    82.0,
    13.0,
    anchor="nw",
    text="时",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    124.0,
    21.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=110.0,
    y=11.0,
    width=28.0,
    height=18.0
)

canvas.create_text(
    167.0,
    13.0,
    anchor="nw",
    text="分",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    211.0,
    21.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=197.0,
    y=11.0,
    width=28.0,
    height=18.0
)

canvas.create_text(
    252.0,
    13.0,
    anchor="nw",
    text="秒",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    294.0,
    21.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=280.0,
    y=11.0,
    width=28.0,
    height=18.0
)

canvas.create_text(
    176.0,
    41.0,
    anchor="nw",
    text="通知标题",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    200.0,
    122.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=135.0,
    y=112.0,
    width=130.0,
    height=18.0
)

canvas.create_text(
    176.0,
    92.0,
    anchor="nw",
    text="通知内容",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    199.0,
    191.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=134.0,
    y=181.0,
    width=130.0,
    height=18.0
)

canvas.create_text(
    176.0,
    140.0,
    anchor="nw",
    text="通知场景",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    56.0,
    160.0,
    anchor="nw",
    text="reminder[默认]，alarm[无效]，incomingCall，urgent",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    199.0,
    255.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=134.0,
    y=245.0,
    width=130.0,
    height=18.0
)

canvas.create_text(
    163.0,
    209.0,
    anchor="nw",
    text="通知留存时间",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    153.0,
    224.0,
    anchor="nw",
    text="long，short[默认]",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    200.0,
    74.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=135.0,
    y=64.0,
    width=130.0,
    height=18.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=wra,
    relief="flat"
)
button_1.place(
    x=164.0,
    y=323.0,
    width=72.0,
    height=20.0
)

window.resizable(False, False)
window.mainloop()