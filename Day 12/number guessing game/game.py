import random
from art import logo
print(logo)
print("Welcome to the number guessing game !!!")
print("I am thinking of a number between 1 to 100")
print("You have to guess the number")
level_chosen = input("Choose the level \n [E] Easy \n [M] Medium \n [H] Hard \n Your level : ").lower()
original_number = random.randint(0, 100)


def game(level):
    print(f'You get {level} chances. Choose Wisely.')
    guessed = 0
    while True:
        guess = int(input('Guess a number : '))
        if guess == original_number:
            print(f'You won!!! You guessed the right number {guess}')
            return
        else:
            guessed += 1
            if guessed == level:
                print(f'You lost !!! I was thinking {original_number}')
                return
            elif guess > original_number:
                print('Too High !!!')
            elif guess < original_number:
                print('Too low !!!')


if level_chosen == 'e':
    chances = 10
elif level_chosen == 'm':
    chances = 7
elif level_chosen == 'h':
    chances = 5
else:
    print('Wrong Input')

game(chances)
