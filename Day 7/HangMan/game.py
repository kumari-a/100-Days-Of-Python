
from hangmanart import stages,logo
from list_of_words import word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)


display = []
guessed=[]
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in guessed:
        print(f"You've already guessed {guess}")
    else:

      for position in range(word_length):
          letter = chosen_word[position]

          if letter == guess:
              display[position] = letter


      if guess not in chosen_word:
          lives -= 1
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          if lives == 0:
              end_of_game = True
              print(f"You lose. The correct word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
    guessed.append(guess)