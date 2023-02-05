import random

def pars_to_number(num):
    try:
        input_number = int(num)
        return input_number
    except ValueError:
        print("Please enter numbers only")
    except BaseException as e:
        print(f"General Error - {e.args}")


def generate_number(max_num):
    return random.randint(1, max_num)


def get_guess_from_user(max_num):
    guess_num = input(f"Please guess a number between 1 to {max_num}: ")
    return pars_to_number(guess_num)


def compare_results(a, b):
    return a == b


def play(difficulty):
    random_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if type(guess) == int:
        return compare_results(random_number, guess)
