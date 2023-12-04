# Win Reminder Assistant v1.2.0

基于 `PySimpleGUI & Windows10/11通知` 的提醒小助手

## Feature

- 支持 `时/分/秒` | `时分秒` 倒计时

- 自定义通知标题和内容

- 自定义通知图标（todo）

- 可选择的通知场景 | [UWP toast](https://learn.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-toast)

- 可选择的前台通知留存时间（long[25s] | short）

## INSTALL

`pip intall -r requirements.txt`

`pyinstaller -F wra.py -i icon.ico -w`