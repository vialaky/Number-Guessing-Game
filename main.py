import random

hidden_number = random.randint(1, 100)

print('Welcome to the Number Guessing Game')


def is_valid(data):
    if data.isdecimal() and 1 <= int(data) <= 100:
        return True
    else:
        return False


while True:
    print('Enter the number:')
    input_data = input()

    if is_valid(input_data):

        number = int(input_data)

        if number < hidden_number:
            print('Your number is less than the hidden number, try again')
        elif number > hidden_number:
            print('Your number is greater than the hidden number, try again')
        else:
            print('You guessed it, congratulations!')
            break
    else:
        print('Maybe we’ll still enter an integer from 1 to 100?')

print('Thanks for playing the number guessing game. See you...')
