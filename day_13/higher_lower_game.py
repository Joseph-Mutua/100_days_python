from art import logo, vs
from game_data import data
import random

players = []
score = 0
keep_playing=True


def generate_char():
    random_char = random.choice(data)
    return random_char


for _ in range(2):
    players.append(generate_char())


def char_name(char):
    return char["name"]


def char_followers(char):
    return char["follower_count"]


def char_desc(char):
    return char["description"]


def char_country(char):
    return char["country"]


char_a = players[0]
char_b = players[1]

while char_a == char_b:
    char_b = generate_char()





# print(logo)
print(
f"Compare A {char_name(char_a)}, a {char_desc(char_a)} from {char_country(char_a)}\n "
)
print(vs)
print(
    f"Against B {char_name(char_b)}, a {char_desc(char_b)} from {char_country(char_b)} "
)
user_choice = input("Who has more followers? Type 'A' or 'B': ")


if user_choice == "A":
    user_char = players[0]
    other_char = players[1]
elif user_choice == "B":
    user_char = players[1]
    other_char = players[0]

print(
        f"Compare A {char_name(user_char)}, a {char_desc(user_char)} from {char_country(user_char)}\n "
    )
print(vs)
print(
    f"Against B {char_name(other_char)}, a {char_desc(other_char)} from {char_country(other_char)} "
)


if char_followers(user_char) > char_followers(other_char):
    score += 1
    print(f"You're right! Current Score is {score}")
    players.remove(other_char)
    players.append(generate_char())
    user_char = players[0]
    other_char = players[1]
    keep_playing = True

else:
    print(f"Sorry, that's wrong. Final score: {score}")
    keep_playing = False




def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

     
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
