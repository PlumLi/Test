#!/vtest/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午9:11
# @Author  : PlumLi
# @Contact : 
# @File    : run.py
# @esc     :

from flask import Flask
from flask import render_template#基于jinja2
from flask import request


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


if __name__ == '__main__':
    app.run(debug=True)
