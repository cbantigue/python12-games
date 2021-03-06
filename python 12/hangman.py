import random
from words import words # imported from words.py
import string 

def choose_valid_word(words):
    word = random.choice(words)
    while 'kwantlen' or 'rai' or 'zimmerman' in word: #skips 'kwantlen', 'rai', & 'zimmerman'
        word = random.choice(words)

    return word

def hangman(): 
    word = choose_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() 

#getting user input 
user_letter = input("Guess a letter: ").upper()
if user_letter in alphabet - used_letters:
    used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)

elif user_letter in used_letters:
    print('Character already guessed. Try again. ')
else:
    print('Invalid character. Try again' )

user_input = input("Type something: ")
print(user_input) 
