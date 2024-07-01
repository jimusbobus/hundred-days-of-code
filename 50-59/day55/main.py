from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        result = f"<b>{function()}</b>"
        return result

    return wrapper


def make_italic(function):
    def wrapper():
        result = f"<em>{function()}</em>"
        return result

    return wrapper


def make_underlines(function):
    def wrapper():
        result = f"<u>{function()}</u>"
        return result

    return wrapper


def style_me(function):
    def wrapper(*args, **kwargs):
        return f"<{kwargs['style']}>{function(kwargs['style'])}</{kwargs['style']}>"
    return wrapper


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/bye')
# @make_bold
# @make_underlines
# @make_italic
def bye():
    return "Bye"


@app.route('/hi')
def hi():
    return "Hi"


@app.route('/hi/<style>')
@style_me
def hi_style(s):
    return f"Hi {s}"


@app.route('/<username>/<int:age>')
def hello_user(username, age):
    return f"Hello {username}, you are {age}!"


if __name__ == "__main__":
    app.run(debug=True)
