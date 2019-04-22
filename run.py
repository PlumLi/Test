#!/venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午9:11
# @Author  : PlumLi
# @Contact : 
# @File    : run.py
# @esc     :

from flask import Flask
from flask import render_template#基于jinja2
from flask import request
from APITest import *

app = Flask(__name__)


@app.route('/')#/->定义的页面
def index():
    #处理当前定义的页面的请求响应
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    filename = file.filename
    file.save('static/%s' % filename)
    return 'static/%s' % filename


@app.route('/scancode')
def get_info():
    # get info
    aes = AESHandle()
    info = request.args.get('req')
    if info:
        #aes解密
        info = aes.decrypt(info)
        info = info.split('&')
        #获取入/出场信息，并构建data
        for key in info:
            if key.find('action') == 0:
                action = key.split('action=')[-1]
                if action == 'enter':
                    action = 'E'
                elif action == 'quit':
                    action = 'K'
            elif key.find('parkid') == 0:
                parkid = key.split('parkid=')[-1]
            elif key.find('channel') == 0:
                num = key.split('channel=')[-1]
        channel = '%s%s' % (action, num)
        userid = '001'
        lpn = '京Z000001'
        data = "{\"userid\":\"%s\",\"channel\":\"%s\",\"virtuallpn\":\"%s\"}" \
               % (userid, channel, lpn)


    else:
        print("参数错误")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
