# Play a number game

import random

letter = True
while letter:
    num = input("Type a number for an upper bound:")
    if num.isdigit():
        print("Lets play a game")
        num = int(num)
        letter = False
    else:
        print("Not a number try again!")
number_guess = random.randint(1, num)
guess = None
count = 1
while guess != number_guess:
    guess =input('Please type a number between 1 and ' + str(num) + " : ")
    if guess.isdigit():
        guess =int(guess)


        if guess == number_guess:
            print('You guess the number')
        else:
            print('Please try again')
            count += 1
print('It took you', count, 'guesses!')

