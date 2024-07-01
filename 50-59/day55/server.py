from flask import Flask
import random

app = Flask(__name__)
answer = random.randint(1, 10)


def style_home(function):
    def wrapper():
        result = (f"<h1>{function()}</h1>"
                  f"<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmo2NTVpMGNrOGt4dXY1bTlvYWV6a2RlOTFvcnQwMmloNjhsZmp6MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/DhiRqIsofVMi7fWNBQ/giphy.webp' />")
        return result

    return wrapper


def style_guess(function):
    def wrapper2(*args, **kwargs):
        low_img = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWppM2IyejZ5aXIyaWIxdnEzbXEwOXZpM3U5NHlucWo5M29hOXNzayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BNzJclwvwkhv9xP3un/giphy.gif"
        high_img = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTc3ejNtMTdrZnI5NXdmY25lZGhybW92Z2VmcGxjaG45YmlhczlndSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CBnXOLstPIoTmqLryW/giphy.gif"
        happy_img = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGRndnMwbWg2YzBrbTlwZGN5emM1OXVveWtuYjFuanlyZGRncGcwZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DhstvI3zZ598Nb1rFf/giphy-downsized-large.gif"

        if int(kwargs['guess']) > answer:
            result = (f"<h1 style='color: red;'>Too High, try again!</h1>"
                      f"<img src='{high_img}' />")
        elif int(kwargs['guess']) < answer:
            result = (f"<h1 style='color: purple;'>Too Low, try again!</h1>"
                      f"<img src='{low_img}' />")
        else:
            result = (f"<h1 style='color: green;'>You got it</h1>"
                      f"<img src='{happy_img}' />")

        return result

    return wrapper2


@app.route('/')
@style_home
def home():
    global answer
    answer = random.randint(1, 10)
    return "Guess a number between 0 and 9"


@app.route('/<int:guess>')
@style_guess
def player_guess(guess):
    print(f"The guess was {guess}, the generated value was {answer}")
    return guess



if __name__ == "__main__":
    app.run(debug=True)
