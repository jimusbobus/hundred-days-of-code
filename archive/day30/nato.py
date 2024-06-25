import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(data_dict)


def gen():
    sentence = input("Enter Word.").upper()
    try:
        code = [data_dict[letter] for letter in sentence]
    except KeyError as msg:
        print('Only letters.')
        gen()
    else:
        print(code)


gen()
