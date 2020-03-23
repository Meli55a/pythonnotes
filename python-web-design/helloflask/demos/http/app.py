import os
from urllib.parse import urlparse, urljoin
from flask import Flask, request, redirect, url_for, abort, make_response, session, abort
from jinja2.utils import generate_lorem_ipsum

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'secret string')


@app.route('/')
@app.route('/hello')
def hello():
    # name = request.args.get('name', 'Flask')  # 获取查询参数 name 的值
    # return '<h1>hello, %s!</h1>' % name
    # return '', 302, {'Location', 'http://www.example.com'}
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = '<h1>Hello, %s</h1>' % name
        # 根据用户认证状态返回不同的内容
        if 'logged_in' in session:
            response += '[Authenticated]'
        else:
            response += '[Not Authenticated]'
    return response


@app.route('/goback/<int:year>')
def go_back():
    return "<p> Welcome to %d!</p>" % (2018 - year)


@app.route('/colors/<any(blue, white, red):color>')
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>'


@app.route('/hi')
def hi():
    return redirect(url_for('hello'))


@app.route('/404')
def not_found():
    abort(404)


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True  # 写入 session
    return redirect(url_for('hello'))


@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page'


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if target:
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return '''
    <h1> A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script type="text/javascript">
    $(function(){
        $('#load').click(function(){
            $.ajax({
                url: '/more',
                type: 'get',
                success: function(data){
                    $('.body').append(data);
                }
            })
        })
    })
    < / script > ''' % post_body
    
@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)