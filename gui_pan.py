#!/vtest/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午10:15
# @Author  : PlumLi
# @Contact : 
# @File    : gui_pan.py
# @esc     : 
from tkinter import *
from tkinter.filedialog import *
import urllib


def upload():
    filename = askopenfilename()
    url = "http://127.0.0.1:5000/upload"
    data = '''-----------------------------1469225038527020311763521840
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: text/plain
%s
-----------------------------1469225038527020311763521840--''' % (filename.split('/')[-1])


root = Tk()
root.title("网盘")
ent = Entry(root, width=40)#输入框控件
ent.grid()
btn_upload = Button(root, text=" 上 传 ", command=upload)
btn_upload.grid()
btn_download = Button(root, text=" 下 载 ")
btn_download.grid()
mainloop()
