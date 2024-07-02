from flask import Flask, render_template, request, redirect, url_for
import sqlite3

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

@app.route('/')
def home():
    print(all_books)
    print(len(all_books))
    return render_template("index.html", books=all_books, number_books=len(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)

        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

