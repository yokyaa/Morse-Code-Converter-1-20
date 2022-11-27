# MORSE CODE PROJECT

import pandas

# Print welcoming message.
print('Welcome to Morse Code Converter.')

# Make a dictionary for each letter to morse code.
data = pandas.read_csv('morse_alphabet.csv')
data_frame = pandas.DataFrame(data)

dictionary_list = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# Get the input and convert it to morse code through your dictionary.
is_on = True
while is_on:
    word = input("Type your message Text here ('/'means Space between words) :  ").upper()
    try:
        results = [dictionary_list[item] for item in word]
        # Give feedback to user  converted morse code.
        print(f"{results}")
        ask = input("Do you want to convert another letter? Y or N: ").upper()
        # Ask for another question or exiting app.
        if ask == 'Y' or ask == 'YES':
            is_on = True
        else:
            is_on = False
    except KeyError:
        print("Only English alphabet letter or (:.'!?$/)")
