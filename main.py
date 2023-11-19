import random


def guess_a_number():
    print('𝔾𝕦𝕖𝕤𝕤 𝔸 ℕ𝕦𝕞𝕓𝕖𝕣:')
    guess = False

    def choice():
        if guessed_number == number:
            print('Right Choice. You Won...')
        elif guessed_number > number:
            print('Your guess is too high.')
        elif guessed_number < number:
            print('Your guess is too low.')

    while not guess:
        number = random.randint(0, 50)
        level = (input("Select the level of difficulty. Type 'easy' or 'hard': ")).lower()
        if level == 'easy':
            lives = 10
            print(f"You've {lives} attempts to play the game")
            guessed_number = int(input('Guess a number between 0 to 50: '))
            choice()
            while lives != 0:
                if guessed_number != number:
                    lives = lives - 1
                    if lives != 0:
                        print(f'You have {lives} attempts to play.')
                        guessed_number = int(input('Guess a number between 0 to 50: '))
                        choice()
                elif guessed_number == number:
                    guess = True
            if lives == 0:
                print("You're out of lives, You lost!")
                break
            if guess == True:
                print(f'Hurray, You Won!. The number was {number}')
                break
        elif level == 'hard':
            lives = 5
            print(f"You've {lives} attempts to play the game")
            guessed_number = int(input('Guess a number between 0 to 50: '))
            choice()
            while lives != 0:
                if guessed_number != number:
                    lives = lives - 1
                    if lives != 0:
                        print(f'You have {lives} attempts to play.')
                        guessed_number = int(input('Guess a number between 0 to 50: '))
                        choice()
                elif guessed_number == number:
                    guess = True
            if lives == 0:
                print("You're out of lives, You lost!")
                break
            if guess == True:
                print(f'Hurray, You Won! The number was {number}')
                break


guess_a_number()
