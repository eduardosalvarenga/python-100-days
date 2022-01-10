# Create a NATO Alphabet project using dictionary and list comprehension with pandas

import pandas

nato_phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

data = pandas.DataFrame(nato_phonetic_alphabet)

nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    try:
        phonetic_list = [nato_dictionary.get(letter) for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
