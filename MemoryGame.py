import random
import time
import sys

def pars_to_number(num):
    try:
        input_number = int(num)
        return input_number
    except ValueError:
        print("Please enter numbers only")
    except BaseException as e:
        print(f"General Error - {e.args}")


def generate_sequence(num_of_numbers):
    rand_list = []
    for i in range(num_of_numbers):
        rand_list.append(random.randint(1, 101))
    return rand_list


def get_list_from_user(num_of_numbers):
    user_list = []
    for i in range(num_of_numbers):
        valid_num = False
        while not valid_num:
            num = input("Please enter a number: ")
            num_int = pars_to_number(num)
            if type(num_int) == int:
                valid_num = True
                user_list.append(num_int)
    return user_list


def is_list_equal(list_a, list_b):
    equal_list = True
    for num in list_a:
        if num not in list_b:
            equal_list = False
    return equal_list


def play(difficulty):
    list_of_random_numbers = generate_sequence(difficulty)
    print(list_of_random_numbers)
    time.sleep(0.7)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    list_of_user_numbers = get_list_from_user(difficulty)
    return is_list_equal(list_of_user_numbers, list_of_random_numbers)