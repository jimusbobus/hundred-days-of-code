from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=posts.get_posts())


@app.route('/post/<post_id>')
def show_post(post_id):
    post = posts.get_post(post_id)
    print(f"DEBUG: POST: {post}")
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
