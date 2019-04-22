#!/venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午10:15
# @Author  : PlumLi
# @Contact : 
# @File    : gui_pan.py
# @esc     : 
from tkinter import *
from tkinter.filedialog import *
import urllib.request
import urllib.response
import urllib.parse

def upload():
    filename = askopenfilename()

    url = "http://127.0.0.1:5000/upload"
    data = '''------WebKitFormBoundarygAODS5NgAM4O0d1I
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: application/octet-stream

[file]
------WebKitFormBoundarygAODS5NgAM4O0d1I--''' % filename.split('/')[-1]
    with open(filename, 'rb') as f:
        file = f.read()
    data = data.encode().replace('[file]'.encode(), file)

    req = urllib.request.Request(url, data)
    req.add_header("Content-Type", "multipart/form-data; boundary=----WebKitFormBoundarylH3DR2Tvdx6APu99")
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)


root = Tk()
root.title("网盘")
ent = Entry(root, width=40)#输入框控件
ent.grid()
btn_upload = Button(root, text=" 上 传 ", command=upload)
btn_upload.grid()
btn_download = Button(root, text=" 下 载 ")
btn_download.grid()
mainloop()
