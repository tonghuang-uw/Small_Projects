import numpy as np
import random

"""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
"""

def main():
    """
    """
    explanation = """
    When I say:     That means:
     Pico           One digit is correct but in the wrong position.
     Fermi          One digit is correct and in the right position.
     Bagels         No digit is correct.

    For example, if the secret number was 248 and your guess was 843,
    clues would be Fermi Pico.

    """
    print("I am thinking of a 3-digit number. Try to guess it.")
    print("Here are the rules:")
    print(explanation)
    print("I have thought up a number.")
    print(" You have ten 10 guesses to get it.")
    
    max_guess = 10
    while True:
        n_guess = 1
        correct_answer = random.randint(100, 999)
        while n_guess <= max_guess:
            guess_user = guess_from_user(n_guess)
            if guess_user == 's':
                break
            clue = compare(correct_number=correct_answer, guess = guess_user)
            n_guess += 1
            print(clue)
            if guess_user == correct_answer:
                break
        print("Correct Answer: {}".format(correct_answer))
        user_input = input("Do you want to continue to play: (yes or no)").lower()
        if user_input == "yes":
            continue
        elif user_input == "no":
            play = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'!")



def guess_from_user(n):
    try:
        number = int(input(f'Guess #{n}:'))
    except ValueError:
        print("That was not an integer. Please enter an integer number.")
    return number

def compare(correct_number, guess):
    correct_number = str(correct_number)
    guess = str(guess)
    clue = []
    if correct_number == guess:
        return 'You got it!'
    for num, gue in zip(correct_number, guess):
        if num  == gue:
            clue.append('Fermi')
        elif gue in correct_number:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'
    else:
        clue.sort()
        return ' '.join(clue)

if __name__ == "__main__":
    main()