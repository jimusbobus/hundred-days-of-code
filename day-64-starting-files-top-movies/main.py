from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests
import urllib.parse
import os

api_key = os.getenv('TMDB_API_KEY')
if not api_key:
    raise ValueError("No API key found. Please set the TMDB_API_KEY environment variable.")

request_params = {
    "api_key": api_key
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DATABASE
class DataBase(DeclarativeBase):
    pass


# CREATE TABLE
db = SQLAlchemy(model_class=DataBase)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-ten-movies.db"
db.init_app(app)


# Define a class that maps to a table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    tmdb_rating: Mapped[float] = mapped_column(nullable=True)
    my_rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)

    # # String representation for the model (optional)
    def __repr__(self):
        return f"<Movie(id='{self.id}', title='{self.title}', my_rating='{self.my_rating}, ranking='{self.ranking}')>"


class AddMovieForm(FlaskForm):
    title = StringField("Enter the Movie Title")
    submit = SubmitField("Done")


class RateMovieForm(FlaskForm):
    my_rating = StringField("Your Rating Out of 10, e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.my_rating)).scalars().all()
    for index, movie in enumerate(movies, start=0):  # start=1 begins numbering from 1
        movies[index].ranking = len(movies) - index  # set the ranking to match my_rating
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm(obj=movie)
    if form.validate_on_submit():
        # Populate the movie object with data from the form
        form.populate_obj(movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST":
        encoded_movie_title = urllib.parse.quote(request.form['title'])
        search_url = f'https://api.themoviedb.org/3/search/movie?query={encoded_movie_title}'
        search_results = requests.get(search_url, params=request_params).json()
        return render_template("select.html", movie_list=search_results['results'])
    return render_template("add.html", form=form)


@app.route("/list_movies", methods=["GET", "POST"])
def list_movies(movie_list):
    return render_template("select.html", movie_list=movie_list)


@app.route("/select_movie/<int:tmdb_id>", methods=["GET", "POST"])
def select_movie(tmdb_id):
    search_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}'
    search_response = requests.get(search_url, params=request_params)
    search_results = search_response.json()
    # print(f"DEBUG: Data:\n{json.dumps(search_results, indent=4)}")
    new_movie = Movie(
        title=search_results['original_title'],
        year=search_results['release_date'],
        description=search_results['overview'],
        tmdb_rating=search_results['vote_average'],
        img_url=f"https://image.tmdb.org/t/p/w500/{search_results['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
