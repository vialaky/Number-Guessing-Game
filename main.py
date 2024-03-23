import random

random_number = random.randint(1, 100)

print('Welcome to the Number Guessing Game')


def is_valid(input_data):
    if input_data.isdecimal() and 1 <= int(input_data) <= 100:
        return True
    else:
        return False


while True:
    print('Enter the number:')
    data = input()

    if is_valid(data):
        print('YES')
        number = int(data)
    else:
        print('Maybe we’ll still enter an integer from 1 to 100?')
