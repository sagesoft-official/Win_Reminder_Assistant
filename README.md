<!--
 * @Author: Nya-WSL
 * Copyright © 2023 by Nya-WSL All Rights Reserved. 
 * @Date: 2023-12-05 00:14:12
 * @LastEditors: 狐日泽
 * @LastEditTime: 2023-12-13 14:02:31
-->
# Win Reminder Assistant

基于 `Tkinter/nicegui & Windows10/11通知` 的提醒小助手

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

```
cd web/
pip intall -r requirements.txt
python build.py
```

## KNOWN ISSUES

- 无法存储中文数据，等待nicegui官方回复再考虑如何修复