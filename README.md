<!--
 * @Author: Nya-WSL
 * Copyright © 2023 by Nya-WSL All Rights Reserved. 
 * @Date: 2023-12-05 00:14:12
 * @LastEditors: 狐日泽
 * @LastEditTime: 2023-12-12 22:28:22
-->
# Win Reminder Assistant

基于 `Tkinter & Windows10/11通知` 的提醒小助手

## Feature

- 支持 `时/分/秒` | `时分秒` 倒计时

- 自定义通知标题和内容

- 自定义通知图标（考虑到需求，暂无支持计划）

- 可选择的通知场景 | [UWP toast](https://learn.microsoft.com/en-us/uwp/schemas/tiles/toastschema/element-toast)

- 可选择的前台通知留存时间（long[25s] | short[默认，时间未知]）

## INSTALL

#### WRA

`pip intall -r requirements.txt`

`pyinstaller -F wra.py -i icon.ico -w`

#### WRA_WebL

`python build.py`

## KNOWN ISSUES

- WRA-WebL在计时未结束的时候无法终止计时
- 如果在计时期间再一次计时将会启动两个计时器
- 可以通过结束进程的方式强制结束上一次计时