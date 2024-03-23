import random

random_number = random.randint(1, 100)

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
        print('YES')
        number = int(input_data)
    else:
        print('Maybe we’ll still enter an integer from 1 to 100?')
