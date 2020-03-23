- `helloflask/hello/app.py`：最小的 Flask 程序

```python
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'
```
- 程序的主模板一般命名为：`app.py`，也可以为其它的，但不能使用 `flask.py`

- 实例化
- 路由：
  - 为函数附加 `app.route()` 装饰器，并传入 URL 规则作为参数，我们就可以让 URL 与函数建立关联, 称为 **注册路由**
  - 路由负责管理 URL 和函数之间的映射，而这个函数则被称为**视图函数**（view function）
  - 在这个程序里，`app.route()` 装饰器把根地址`/` 和 `index()` 函数绑定起来，当用户访问这个 URL 时就会触发 `index()`函数
  - 视图函数返回的值将作为响应的主体，一般来说，响应的主体就是呈现在浏览器窗口的 HTML 页面
  - route() 装饰器的第一个参数是** URL 规则**，用字符串表示，必须以斜杠（/）开始
  - 一个视图函数可以绑定多个URL 
    ```python
        @app.route('/hi')
        @app.route('/hello')
        def say_hello():
            return '<h1>Hello, Flask!</h1>'
        ```
  - 动态URL
    ```python
    # 动态 URL，<name>为变量
    @app.route('/greet', defaults={'name': 'Programmer'}) # 设置默认参数
    @app.route('/greet/<name>')
    def greet(name):
        return '<h1>Hello, %s!</h1>' % name
    ```