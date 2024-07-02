from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)


# CREATE DATABASE
class DataBase(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=DataBase)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


# Define a class that maps to a table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)  # An integer primary key column
    title: Mapped[str] = mapped_column(unique=True)  # A string column for the title
    author: Mapped[str] = mapped_column(unique=True)  # A string column for the author
    rating: Mapped[float] = mapped_column(unique=True)  # A string column for the rating

    # # String representation for the model (optional)
    def __repr__(self):
        return f"<User(id={self.id}, title='{self.title}', author='{self.author}, rating='{self.rating}')>"


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars().all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == 'POST':
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)


@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
