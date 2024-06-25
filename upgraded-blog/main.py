from flask import Flask, render_template, request
from post import Post
import SendMessage
import json

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=posts.get_posts())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact(successfully_sent=False):
    if request.method == "POST":
        new_contact = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "message": request.form.get("message"),
        }
        SendMessage.send_email("New Contact Requested.", json.dumps(new_contact, indent=4))
        return render_template("contact.html", successfully_sent=True)
    else:
        return render_template("contact.html")


@app.route('/post/<post_id>')
def show_post(post_id):
    post = posts.get_post(post_id)
    print(f"DEBUG: POST: {post}")
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
