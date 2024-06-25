import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(direction, text, shift):
    new_string = ""
    for index in range(len(text)):
        character = text[index]
        if character not in alphabet:
            new_string += character
        else:
            if direction == "encode":
                shifted_index = alphabet.index(character) + shift
                if shifted_index >= len(alphabet):
                    shifted_index = shifted_index - len(alphabet)
            else:
                shifted_index = alphabet.index(character) - shift
                if shifted_index < 0:
                    shifted_index = shifted_index + len(alphabet)
            shifted_character = alphabet[shifted_index]
            new_string += shifted_character

    print(f"{direction} data: {new_string}")

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# decrypt(text, shift)

print(art.logo)

print(f"1 % 26: {1 % 26}")
print(f"2 % 26: {2 % 26}")
print(f"12 % 26: {12 % 26}")
print(f"26 % 26: {26 % 26}")
print(f"27 % 26: {27 % 26}")
print(f"30 % 26: {30 % 26}")

# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     caesar(direction, text, shift)
#
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart != "yes":
#         break
