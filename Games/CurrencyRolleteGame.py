from currency_converter import CurrencyConverter
import random

def pars_to_number(num):
    try:
        input_number = int(num)
        return input_number
    except ValueError:
        print("Please enter numbers only")
    except BaseException as e:
        print(f"General Error - {e.args}")

def get_usd_to_ils():
    cr = CurrencyConverter()

    return cr.convert(1,'USD', 'ILS')


def get_money_interval(difficulty, usd_to_ils_rate ,total_value_of_money):
    interval = ((total_value_of_money - (5-difficulty))*usd_to_ils_rate, (total_value_of_money + (5-difficulty))*usd_to_ils_rate)

    return interval

def get_guess_from_user(total_value_of_money):
    valid_input = False
    while not valid_input:
        guess = input(f'''How many ILS is {total_value_of_money} USD: ''')
        guess = pars_to_number(guess)
        if type(guess) == int:
            valid_input = True
    return guess


def play(difficulty):
    total_value_of_money = random.randint(1, 100)
    usd_to_ils = get_usd_to_ils()
    money_interval = get_money_interval(difficulty, usd_to_ils, total_value_of_money)
    user_guess = get_guess_from_user(total_value_of_money)
    if money_interval[0] <= user_guess <= money_interval[1]:
        return True
    else:
        return False