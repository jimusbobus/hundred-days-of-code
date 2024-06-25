# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

INVITED_NAMES = "./input/Names/invited_names.txt"
TEMPLATE = "./input/Letters/starting_letter.txt"
NEW_LETTER_LOCATION = "./Output/ReadyToSend/"
NEW_LETTER_FILENAME_TEMPLATE = "letter_for_[name].txt"


def get_names():
    _names_list = []
    with open(INVITED_NAMES, mode='r') as _file:
        for _line in _file:
            _names_list.append(_line.strip())

    return _names_list


def get_template():
    with open(TEMPLATE, mode='r') as _file:
        return _file.read()


def write_letter(_new_letter_file, _new_letter):
    with open(_new_letter_file, mode='w') as _file:
        _file.write(_new_letter)


letter_template = get_template()

for name in get_names():
    _new_letter_file = NEW_LETTER_LOCATION + NEW_LETTER_FILENAME_TEMPLATE.replace('[name]', name)
    _new_letter = letter_template.replace('[name]', name)
    write_letter(_new_letter_file, _new_letter)
