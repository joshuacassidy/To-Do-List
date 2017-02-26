import random
import os
import sys

def clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')
def exitGame():
    print("Thanks for playing")
    sys.exit()

def startGame():
    clear()
    print('Welcome to numbers guessing game!')
    playGame = input('Do you want to play? Y/N? ')
    clear() if playGame.lower() != 'n' else exitGame()

    print('The default numbers for this guessing game are between one and ten.')
    print('However if you want you can set your own numbers to guess between.')
    print('Do you want to choose the range of numbers you can guess between?')
    choice = input('Y/N? ')
    if choice.lower() == 'y':
        lowest = int(input('What will your lowest number be? '))
        highest = int(input('What will your highest number be? '))
        num = random.randint(lowest,highest)


    else:
        lowest = 1
        highest = 10
        num = random.randint(lowest,highest)
    print('Your lowest number will be: {} and Your highest number will be: {}.'.format(lowest,highest))
    start = input("Press enter/return to Continue ").lower()
    clear()
    print('The default amount of guesses you can make is 5')
    print('However you can choose how many guesses you can make.')
    print('Would you like to choose how many guesses you can make?')
    guessChoice = input('Y/N? ')
    if guessChoice.lower() == 'y':
        amountOfGuesses = int(input('how many guesses would you like? '))
    else:
        amountOfGuesses = 5
    print('The amountOfGuesses has been set to {}'.format(amountOfGuesses))
    start = input("Press enter/return to Continue ").lower()
    clear()
    guesses = []
    counter = 0
    sameGuess = 0
    counter = amountOfGuesses
    while counter > 0:



        try:
            print("Guess a number between {} and {}. You have {} guesses left out of {}.".format(lowest,highest,counter,amountOfGuesses))
            guess = int(input("What is your {} guess? ".format(len(guesses) + 1)))
            print('')
        except ValueError:
            print("{} isn't a number.".format(guess))
        else:

            if guess == num:
                print("You got it on guess {}".format(len(guesses) + 1))
                print('')
                break
            elif guess in guesses:
                print('You have already guessed {}.'.format(guess))
                print('')
                print('Your guesses so far: ')
                for number in guesses:
                    print(number,end=' , ')
                print('\n\n')
                continue
            elif guess < num:
                print("The number is higher than {}. ".format(guess))
                print('')
                counter-=1
            else:
                print("The number is lower than {}.".format(guess))
                print('')
                counter-=1
            guesses.append(guess)
            print('Your guesses so far: ')
            for number in guesses:
                print(number,end=' , ')
            print('\n\n')
    else:
        print("The number was {}.".format(num))
    playAgain = input("Would you want to play again? Y/N: ")
    startGame() if playAgain.lower() == 'y' else exitGame()

startGame()
