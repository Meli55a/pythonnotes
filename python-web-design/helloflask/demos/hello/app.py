# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)  # 实例化一个 Flask 实例
app.debug = True


@app.route('/')  # 注册路由
def index():
    return '<h1>Hello Flask!</h1>'  # 返回主体

# 为视图绑定多个 URL
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'

# 动态 URL，<name>为变量
@app.route('/greet', defaults={'name': 'Programmer'})  # 设置默认参数
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name
