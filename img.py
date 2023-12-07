'''
Author: Nya-WSL
Copyright © 2023 by Nya-WSL All Rights Reserved. 
Date: 2023-12-07 10:28:56
LastEditors: 狐日泽
LastEditTime: 2023-12-07 10:51:45
'''
import base64
open_icon = open("icon.ico","rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = f"img = {b64str}"
print(write_data)
f = open("tmp.py","w+")
f.write(write_data)
f.close()