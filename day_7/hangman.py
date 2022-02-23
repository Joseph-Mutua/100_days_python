# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# chosen_word = random.choice(word_list)
# guess = input("Guess any letter:\n").lower()
# print(chosen_word)

# for char in chosen_word:
#     if char == guess:
#         print("True")
#     else:
#         print("False")


# TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


# TODO-5: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters
# chosen word and "display has no more blanks. You  can tell the user they've won"

# TODO-6: - Create a variable called "lives" to keep track of the no of lives
# TODO-7 - If guess is not in chosen word, reduce the lives by 1.
# If the lives go down to 0, then stop the game and print "You Lose!!"


def play_game():
    lives = 6
    chosen_word = random.choice(word_list)
    print(chosen_word)
    new_word = []
    new_word += "_" * len(chosen_word)

    if lives > 0:
        while "_" in new_word:
            guess = input("Guess any letter:\n").lower()
            if guess not in chosen_word:
                lives -= 1
                print("Wrong letter!")
            else:
                for char in range(len(chosen_word)):
                    if chosen_word[char] == guess:
                        new_word[char] = guess
                        print("Correct letter")
                        if lives < 6:
                            lives += 1

            print(stages[lives])
            print(new_word)
        print("You've won!")
    else:
        print("You've lost!")


play_game()
