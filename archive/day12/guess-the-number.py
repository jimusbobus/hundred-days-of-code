# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import helper

MIN_NUMBER = 1
MAX_NUMBER = 100
EASY = 10
HARD = 5

print(helper.LOGO)
print(f"I'm choosing a number between {MIN_NUMBER} and {MAX_NUMBER}!")

answer = random.randint(MIN_NUMBER, MAX_NUMBER)


def set_difficulty():
    level = input("She was a difficulty type easy or hard: ")
    if level == "easy":
        return EASY
    else:
        return HARD


def check_guess():
    player_guess = int(input("Make a guess: "))
    found_number = False
    if player_guess > answer:
        print("Too High.")
    elif player_guess < answer:
        print("Too Low.")
    else:
        found_number = True
        print(helper.WIN)
    return found_number


def game():
    player_difficulty = set_difficulty()
    for guess in range(0, player_difficulty):
        print(f"You have {player_difficulty - guess} attempts remaining to get the number.")
        if check_guess():
            return


game()
