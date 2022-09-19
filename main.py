import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in words or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = getValidWord(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives and used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print('You have already guessed this letter.')
        else:
            print('Invalid character. Try again.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

hangman()