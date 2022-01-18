import random

random_integer = random.randint(1, 10)
random_float = random.random()

print(int(random_float * 2))

A virtual coin toss program
str_arr = ["Heads", "Tails"]
random_int = int(random.random() * 2)

random_choice = str_arr[random_int]
print(random_choice)

# Banker Roulette
names_string = input("Give me everybody's names, separated by a comma.\n")
names_list = names_string.split(",")

random_int = int(random.random() * len(names_list))

random_name = names_list[random_int]

print(random_name)

Using choice()
random_name = random.choice(names_list)

print(random_name)


Index errors and working with nested lists
dirty_dozen = ["Strawberries", "Spinach", "Kales",
               "Nectarines", "Apples", "Grapes",
               "Peaches", "Tomatoes", "Celery", "Potatoes"]

# Treasure Hunt
row1 = ["🤑", "🤑", "🤑"]
row2 = ["🤑", "🤑", "🤑"]
row3 = ["🤑", "🤑", "🤑"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure?\n")

horizontal = int(position[0])
vertical = int(position[1])


map[vertical -1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}\n")


    