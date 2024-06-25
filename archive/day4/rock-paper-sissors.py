rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

ROCK = 0
PAPER = 1
SCISSORS = 2

my_coordinates_dict = {
    ROCK: rock,
    PAPER: paper,
    SCISSORS: scissors
}

player_choice = int(input("What do you choose type 0 for rock, 1 for paper or 2 for scissors."))

if player_choice not in {ROCK, PAPER, SCISSORS}:
    print("Invalid choice, You Lose!")
    exit(1)

print(my_coordinates_dict[player_choice])

computer_choice = random.randint(0, 2)
print("Computer choose: \n" + my_coordinates_dict[computer_choice])

if (player_choice == ROCK and computer_choice == PAPER) or (player_choice == PAPER and computer_choice == SCISSORS) or (
        player_choice == SCISSORS and computer_choice == ROCK):
    print("You Lose")
elif player_choice == computer_choice:
    print("It's a draw")
else:
    print("You Win")
