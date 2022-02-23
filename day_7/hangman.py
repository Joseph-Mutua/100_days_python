# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

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

def play_game():
    chosen_word = random.choice(word_list)
    print(chosen_word)
    new_word = []
    new_word += "_" * len(chosen_word)

    while "_" in new_word:
        guess = input("Guess any letter:\n").lower()
        for char in range(len(chosen_word)):
            if chosen_word[char] == guess:
                new_word[char] = guess
        print(new_word)
   
    print("You've won!!")

play_game()