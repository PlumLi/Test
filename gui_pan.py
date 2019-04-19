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


def upload():
    filename = askopenfilename()
    filename = filename.split('/')[-1]
    print("filename", filename)

    url = "http://127.0.0.1:5000/"
    response = urllib.request.urlopen(url)

    #req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
    #response = urllib.urlopen(req)
    print(response.read().decode('UTF-8'))


root = Tk()
root.title("网盘")
ent = Entry(root, width=40)#输入框控件
ent.grid()
btn_upload = Button(root, text=" 上 传 ", command=upload)
btn_upload.grid()
btn_download = Button(root, text=" 下 载 ")
btn_download.grid()
mainloop()
