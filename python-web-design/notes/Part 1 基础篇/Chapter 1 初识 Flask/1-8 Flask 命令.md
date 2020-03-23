# Flask 命令

> 除了Flask内置的flask run等命令，我们也可以自定义命令

- 通过创建任意一个函数，并为其添加 `app.cli.command()` 装饰器，我们就可以注册一个 flask 命令

```python
@app.cli.command()
def hello():
    click.echo('Hello, Human!')
```
- 函数的名称即为命令名称，这里注册的命令即 `hello`, 运行 `flask hello`
- 也可以在 `app.cli.command()` 装饰器中传入参数来设置命令名称，比如 `app.cli.command（'say-hello'）`会把命令名称设置为`say-hello`，完整的命令即 `flask say-hello`
- 