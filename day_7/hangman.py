#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess any letter:\n").lower()

# for char in chosen_word:
#     if char == guess:
#         print("True")
#     else:
#         print("False")
    

#TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# new_word = " _" * len(chosen_word)
# print(new_word)

# for char in range(0, len(chosen_word)):
#     if chosen_word[char] == guess:
#         new_word.replace(" _", guess)

# print(new_word)

new_word=[]

for char in chosen_word:
    if char == guess:
        new_word.append(guess)
    else:
        new_word.append("_")

print(new_word)
