import GuessGame
import MemoryGame
import CurrencyRolleteGame
import Score


def welcome(name):
    return '''Hello {} and welcome to the World Of Games(WoG).
Here you can find many cool games to play.
'''.format(name)

def validate_input_number(number, min, max):
    min_max_range = range(min, max+1)
    valid = number in min_max_range

    return valid

def print_select_validate_from_menu(msg,min,max):
    input_is_valid = False
    while not input_is_valid:
        print(msg)
        choice = input("Make your choice: ")
        if choice.isnumeric():
            if validate_input_number(int(choice), min, max):
                input_is_valid = True
            else:
                print("Invalid input. Please correct your selection")
        else:
            print("Please enter numbers only")
    return int(choice)

def load_game():
    msg = '''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    '''
    game_choice = print_select_validate_from_menu(msg, 1, 3)
    msg = "Please choose game difficulty from 1 to 5:"
    game_difficulty = print_select_validate_from_menu(msg, 1, 5)

    if game_choice == 1:
        result = MemoryGame.play(game_difficulty)
    elif game_choice == 2:
        result = GuessGame.play(game_difficulty)
    elif game_choice == 3:
        result = CurrencyRolleteGame.play(game_difficulty)

    if result == True:
        Score.add_score(game_difficulty)
        print("Congrats! You Win!!! :)")
    else:
        print("You loose :/ Give it another try?")
