import helper
import random

pack_of_cards: dict[str, int] = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

game = {
    "player": {
        "type": "Player",
        "hand": [],
        "total": 0,
        "bust": False,
        "blackjack": False
    },
    "house": {
        "type": "House",
        "hand": [],
        "total": 0,
        "bust": False,
        "blackjack": False
    }
}


def deal_card(_player_game):
    """Deal a random card from the deck"""
    _new_card = random.choice(list(pack_of_cards.keys()))
    # print(f"DEBUG: New card is {_new_card}")
    # add the card to the player hand
    _player_game['hand'].append(_new_card)
    # update the player total
    _player_game['total'] += pack_of_cards[_new_card]
    # if we have more than 2 cards teh game is in progress and being bust is possible
    if len(_player_game['hand']) > 2:
        if ("Ace" in _player_game['hand']) and _player_game['total'] > 21:
            _player_game['hand'] = change_ace_11_to_1(_player_game['hand'])
            _player_game['total'] = _player_game['total'] - 10
        elif _player_game['total'] > 21:
            _player_game['bust'] = True
    # check if we have blackjack
    if _player_game['total'] == 21:
        _player_game['blackjack'] = True
    # print(f"DEBUG: {_player_game}")


def deal_new_game():
    """Deal a hand to the player and the banker.
    """
    # we rest all the setting here as the game has been started again.
    for _player in game:
        game[_player]['hand'] = []
        game[_player]['total'] = 0
        game[_player]['bust'] = False
        game[_player]['blackjack'] = False
        deal_card(game[_player])
        deal_card(game[_player])
        # print(f"DEBUG: Hand: _ame[_player]")
    return game


def change_ace_11_to_1(_cards: list[str]):
    """Swap 1 Ace from being value 11 to 1."""
    _new_hand = []
    _swapped_ace = False
    for _card in _cards:
        print(f"DEBUG: card is {_card}")
        if _card == "Ace" and not _swapped_ace:
            _new_hand.append("Ace(1)")
            _swapped_ace = True
        else:
            _new_hand.append(_card)
    print(f"DEBUG: New cards: {_new_hand}")
    return _new_hand


def play_hand(_player_game):
    """For the supplied player_game play the hand till we stick / blackjack or are bust"""
    while True:
        player_choice = input(f"{_player_game['type']} - Stick 's' or Twist 't'?").lower()
        if player_choice == "t":
            deal_card(_player_game)
            print(f"{_player_game['type']} Hand is: {_player_game['hand']}")
        else:
            break

        if _player_game['bust'] or _player_game['blackjack']:
            break


house_wins = True
while True:
    game_choice = input("Do you wish to play a hand of BlackJack? (y): ")
    if game_choice != "y":
        break
    helper.clear_screen()
    print(helper.logo)
    game = deal_new_game()
    print(f"Player Hand is: {game['player']['hand']}")
    print(f"House First Card is: {game['house']['hand'][0]}")
    print("------------------------------")

    house_wins = True

    play_hand(game['player'])
    print(f"Player Hand is: {game['player']['hand']}")

    if not game['player']['bust']:
        print(f"House Hand is: {game['house']['hand']}")
        play_hand(game['house'])

        if game['player']['total'] > game['house']['total'] or game['house']['bust']:
            house_wins = False

    print("=============================")
    print(f"Player Hand is: {game['player']}")
    print(f"House Hand is: {game['house']}")
    if house_wins:
        print("House Wins!")
    else:
        print("Player Wins!")
    print("=============================")
