import random


def set_upper_limit():
    """
    Sets the upper limit of the range of numbers for the game.
    """
    print('Specify the upper limit of the range:')
    user_limit = input()
    while not user_limit.isdecimal():
        print('Not integer. Try again')
        user_limit = input()
    return int(user_limit)


def is_valid(data):
    """
    Checks that the user input is an integer within the specified range.
    """
    if data.isdecimal() and 1 <= int(data) <= upper_limit:
        return True
    else:
        return False


# Start the game
print('Welcome to the Number Guessing Game!')

upper_limit = set_upper_limit()
hidden_number = random.randint(1, upper_limit)
wanna_replay = True
attemp_counter = 0

while wanna_replay:

    print(f'Enter an integer from 1 to {upper_limit}:')
    input_data = input()

    if is_valid(input_data):

        number = int(input_data)
        attemp_counter += 1

        if number < hidden_number:
            print('Too low, try again')
        elif number > hidden_number:
            print('Too high, try again')
        else:
            print('You guessed it, congratulations!')
            print('Number of attempts:', attemp_counter)
            print('Wanna replay (Y/N)?')
            if input().lower() == 'y':
                print()
                attemp_counter = 0
                hidden_number = random.randint(1, upper_limit)
            else:
                wanna_replay = False
                break

    else:
        print('Maybe we’ll still enter an integer from 1 to 100?')

print('Thanks for playing the number guessing game. See you...')

# upper_limit = input()
#
# while not upper_limit.isdecimal():
#     # print('Not integer. Try again')
#     upper_limit = input()
#
# upper_limit = int(upper_limit)
#


# game()
