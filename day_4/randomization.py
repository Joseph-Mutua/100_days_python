import random

# random_integer = random.randint(1, 10)
# random_float = random.random()

# print(int(random_float * 2))

# A virtual coin toss program
# str_arr = ["Heads", "Tails"]
# random_int = int(random.random() * 2)

# random_choice = str_arr[random_int]
# print(random_choice)

# Banker Roulette
names_string = input("Give me everybody's names, separated by a comma.\n")
names_list = names_string.split(",")

random_int = int(random.random() * len(names_list))

random_name = names_list[random_int]

print(random_name)