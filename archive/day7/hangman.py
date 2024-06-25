import random
import hangman_art
import hangman_words

lives = 6
random_word = random.choice(hangman_words.word_list)
word_length = len(random_word)
display = ['_'] * word_length

all_guessed_letters = []

print(hangman_art.logo)

while ('_' in display) and (lives > 0):

    print(f"The Random word is: {random_word}")
    print(display)
    print(f"You have {lives} left")

    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in str(all_guessed_letters):
        print(f"You have chosen {guessed_letter} before, try another!")
        continue
    else:
        all_guessed_letters += guessed_letter

    found = False
    for position in range(word_length):
        if guessed_letter == random_word[position]:
            display[position] = random_word[position]
            found = True
    if not found:
        lives -= 1

    print(hangman_art.stages[lives])

if lives == 0:
    print("You Loose")

if '_' not in display:
    print("You Win")
