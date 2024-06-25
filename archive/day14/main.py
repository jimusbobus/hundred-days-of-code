import helper
import data
import random


def init_game(_player_score: int):
    """Initialise the game and show score if score > 0"""
    helper.clear_screen()
    print(helper.LOGO)
    if _player_score > 0:
        print(f"Your right current score: {_player_score}")


def select_comparison(_existing_choice=None):
    """Select something to compare, but cannot be thing that has already selected."""
    _choice = random.choice(data.followers)
    # print(f"DEBUG: number of options={len(data.followers)},choice ={_choice}, existing_choice={_existing_choice}")
    if (_existing_choice is not None) and (_choice == _existing_choice):
        # print(f"DEBUG: choice {_existing_choice} already exists, select again.")
        return select_comparison(_existing_choice)
    return _choice


def guess_higher_followers(_choice_a, _choice_b):
    """Guess the higher followers and return if the higher was selected."""
    print(f"Compare A: {_choice_a['name']} a {_choice_a['description']}, from {_choice_a['country']}.")
    print(helper.VS)
    print(f"Against B: {_choice_b['name']} a {_choice_b['description']}, from {_choice_b['country']}.")
    _player_choice = input("Who has the most followers? Type 'A' or 'B': ").upper()
    if (_choice_a['follower_count'] > _choice_b['follower_count']) and (_player_choice == "A"):
        return True
    else:
        return False


def game():
    game_continue = True
    final_score = 0

    while game_continue:
        init_game(final_score)
        choice_a = select_comparison()
        choice_b = select_comparison(choice_a)
        if guess_higher_followers(choice_a, choice_b):
            print(f"Sorry that's wrong final score: {final_score}")
            game_continue = False
        else:
            final_score += 1


game()
