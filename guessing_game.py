import random
import math

def set_user_num(max_num):
    user_num = input("Pick a number 1-{}: ".format(max_num))
    return user_num

def get_computer_guess():
    computer_guess = random.choice(range_of_guesses)
    return computer_guess

def guess_user_number():
    computer_guess = get_computer_guess()
    print("Is {} your number?".format(computer_guess))
    range_of_guesses.remove(computer_guess)

def is_user_num(answer):
    if answer.lower() == 'y':
        return True
    else:
        return False

max_num = input('Please choose a maximum number: ')

range_of_guesses = list(range(1, int(max_num)))
user_num = set_user_num(max_num)
computer_guess_count = 0
max_computer_guesses = math.floor(int(max_num) * 0.5)

while True:

    try:
        guess_user_number()
    except:
        print("You tricked me!")
        break

    answer = input('y/n? ')

    if is_user_num(answer):
        print("You win this time Gadget!")
        break
    else:
        computer_guess_count += 1
        if computer_guess_count == max_computer_guesses:
            print("Sorry, out of guesses!")
            print("My number was {}".format(user_num))
            break
