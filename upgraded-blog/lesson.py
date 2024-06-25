from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("lesson.html")


@app.route('/login', methods=["POST"])
def login():
    name = request.form.get("name")
    password = request.form.get("password")
    return name + password


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
