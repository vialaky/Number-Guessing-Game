import random

random_number = random.randint(1, 100)

print('Welcome to the Number Guessing Game')


def is_valid(input_data):
    if input_data.isdecimal() and 1 <= int(input_data) <= 100:
        return True
    else:
        return False
