import random
from art import logo


def play_game():
    print(logo)
    print("Welcome to the number playing game")
    print("I'm thinking of a number between 1 and 100")

    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_difficulty == 'easy':
        attempts = 10
    elif game_difficulty == 'hard':
        attempts = 5

    correct_guess = random.randint(1, 100)




    while attempts > 0:
        num_guess = int(input("Make a guess:\n"))

        if num_guess == correct_guess:
            print(f"You got it! The answer was {num_guess}")
            break
        elif num_guess < correct_guess:
            print("Too Low")
            print("Guess again")
            attempts -= 1
            print(
                f"You have {attempts } attempts remaining to guess the number")

        elif num_guess > correct_guess:
            print("Too High")
            print("Guess again")
            attempts -= 1
            print(
                f"You have {attempts } attempts remaining to guess the number")
            
    if attempts == 0:
        print(f"You're outta luck buddy. The correct number was {correct_guess}")

play_game()
