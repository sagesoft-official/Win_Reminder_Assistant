'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-12 18:46:54
LastEditors: 狐日泽
LastEditTime: 2023-12-12 22:37:53
'''
import os
import subprocess
from pathlib import Path
import nicegui
import toast

cmd = [
    'pyinstaller',
    '-F', 'WRA_WebL.py', # your main file with ui.run()
    '-w', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui',
    '-p', f'{Path(toast.__file__).parent}\\toast.py',
    '-i', '../icon.ico'
]
subprocess.call(cmd)
