from Live import load_game, welcome

keep_playing = True
name = input("What is your name: ")
print(welcome(name))
while keep_playing:
    load_game()
    keep_playing = input("Do you want to play another game? (Y/N): ").lower() == 'y'

print("Goodbye :)")