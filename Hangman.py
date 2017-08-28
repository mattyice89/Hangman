'''
The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main
goal here is to create a sort of “guess the word” game. The user needs to be
able to input letter guesses. A limit should also be set on how many guesses
they can use. This means you’ll need a way to grab a word to use for guessing.
(This can be grabbed from a pre-made list. No need to get too fancy.) You will
also need functions to check if the user has actually inputted a single letter,
to check if the inputted letter is in the hidden word (and if it is, how many
times it appears), to print letters, and a counter variable to limit guesses.
'''

import random
from sys import exit

print("Let's play hangman.  I'm going to think of a word and you're going to ")
print("try and guess it.  You can have up to 10 incorrect guesses.")
print("Start by guessing a letter.")

def choose_word():
    lines = open('words.txt').readlines()
    line = lines[random.randint(1,851)]
    words = line.split()
    myword = random.choice(words)
    guessed_letters_correct = []
    guessed_letters_incorrect = []
    print(myword)
    guess_check = list(set(myword))
    print(sorted(guess_check))
    while len(guessed_letters_incorrect) < 10 and sorted(set(guessed_letters_correct)) != sorted(guess_check):
        guess = input("> ")
        if guess in guessed_letters_correct or guessed_letters_incorrect:
            print(f"You've already guessed {guess}!  Try again!")
        elif guess in myword and guess not in guessed_letters_correct or guessed_letters_incorrect:
            print(f"Yes, \'{guess}\' is part of the word!")
            guessed_letters_correct.append(guess)
            print("You've guessed ", len(guessed_letters_correct)," correct letter(s).")
            print("The correct letters you've guessed are:")
            print(guessed_letters_correct)
            print("You've guessed ", len(guessed_letters_incorrect)," incorrect letters.")
            print("The incorrect letters you've guessed are:")
            print(guessed_letters_incorrect)
        else:
            print(f"Sorry, {guess} is not part of the word.")
            guessed_letters_incorrect.append(guess)
            print("You've guessed ", len(guessed_letters_correct)," correct letter(s).")
            print("The correct letters you've guessed are:")
            print(guessed_letters_correct)
            print("You've guessed ", len(guessed_letters_incorrect)," incorrect letter(s).")
            print("The incorrect letters you've guessed are:")
            print(guessed_letters_incorrect)
    print("Congratulations, you win! The correct word was:")
    print(myword)

choose_word()
