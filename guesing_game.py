import random

def guessing_game():
    
    name = input('Please, enter your name: ')
    print(f'\nHello, {name}, lets play a guessing game!\n\n')

    rand = random.randint(0, 100)
    
    while True:
        guess = int(input('What number has been chosen?: \n'))
        if rand < guess:
            print('Too high\n')
        elif rand > guess:
            print('Too low\n')
        else:
            print('\nJust right!')
            exit()

guessing_game()