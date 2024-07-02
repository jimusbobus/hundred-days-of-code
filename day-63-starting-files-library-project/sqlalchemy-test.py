# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped, mapped_column
#
# app = Flask(__name__)
#
#
# ##CREATE DATABASE
# class Base(DeclarativeBase):
#     pass
#
#
# db = SQLAlchemy(model_class=Base)
#
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
# # initialize the app with the extension
# # db.init_app(app)
#
#
# # Define a class that maps to a table
# class Books(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)  # An integer primary key column
#     title: Mapped[str] = mapped_column(unique=True)  # A string column for the title
#     author: Mapped[str] = mapped_column(unique=True)  # A string column for the author
#     rating: Mapped[float] = mapped_column(unique=True)  # A string column for the rating
#
#     # # String representation for the model (optional)
#     def __repr__(self):
#         return f"<User(id={self.id}, title='{self.title}', author='{self.author}, rating='{self.rating}')>"
#
#
# with app.app_context():
#     db.create_all()
#     book = Books(
#         title="Harry Potter",
#         author="J. K. Rowling",
#         rating=9.3
#     )
#     db.session.add(book)
#     db.session.commit()
