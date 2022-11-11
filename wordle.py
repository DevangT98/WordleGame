import colorama
from colorama import Fore, Back

word = 'UNITE'
GAME_ON = True

def take_guess():
    guess = input()
    if len(guess)!=5:
        return 'Please guess a 5 letter word'
    return guess


def check_word(word, guess):
    output = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            output += Back.GREEN + guess[i] + Back.RESET
        elif guess[i] in word:
            output += Back.YELLOW + guess[i] + Back.RESET
        else:
            output += Back.BLACK + guess[i] + Back.RESET
            
    return output        


no_of_tries = 0
while no_of_tries < 6:
    guess = take_guess()
    if word == guess:
        print(Back.GREEN + guess + Back.RESET)
        no_of_tries+=6
    else:
        print(check_word(word,guess))
    no_of_tries+=1
    print(" ", end ="\n")
    
        


