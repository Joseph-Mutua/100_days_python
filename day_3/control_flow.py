# Roller Coster
print("Welcome to the rollercoster")
height = int(input("What is your height in cm?\n"))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("what's your age?\n"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")


num = int(input("Input any number you like\n"))

if num % 2 == 0:
    print("That's an even number")
else:
    print("That's an odd number")


# BMI Calculator
print("Welcome to the BMI calculator\n")
weight = input("Please inpt your weight?\n")
height = input("What's your height?\n")
bmi_index = int(float(weight) / float(height)**2)

if bmi_index < 18.5:
    print("Your BMI index is " + str(bmi_index) +
          " which means you're UNDERWEIGHT")
elif bmi_index < 25:
    print("Your BMI index is " + str(bmi_index) +
          " which means you have a NORMAL WEIGHT")
elif bmi_index < 30:
    print(f"Your BMI index is {bmi_index} which means you're OVERWEIGHT")
elif bmi_index < 35:
    print(f"Your BMI index is {bmi_index} which means you're OBESE")
else:
    print(f"You're clinically obese")


# Leap year Calculator
print("Welcome to the leap year calculator")

year = int(input("Please type in any year to check whether it's a leap year\n"))

if year %4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That's a leap year")
        else:
            print("That's not a leap year")
    else:
        print("That's a leap year")
else:
    print("that's not a leap year")


# Pizza shop
pizza_order = input(
    "Please input your pizza order. Type s for small, m for medium and l for large pizza\n")
extra_pep = input("Do you want pepperoni? Type y or n\n")
total_bill = 0

extra_cheese = input("Do you need extra cheese? Type y or n\n")

if extra_cheese == "y":
    total_bill += 1
else:
    total_bill += 0


if pizza_order == "s":
    total_bill += 15
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 2} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
elif pizza_order == "m":
    total_bill += 20
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 3} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
elif pizza_order == "l":
    total_bill += 25
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 3} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
else:
    print("You need to make an order please")


# Love Calculator

print("Welcome to the love calculator\n")
name1 = input("Wha's your name? \n")
name2 = input("what's their name?\n")

combined_string = name1 + name2

lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(
        f"Your love score is {love_score}. You go together like coke or metos")
elif (40 <= love_score >= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")



# Treasure Island Game
print('''
 _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to the Treasure Island")
print("your mission is to find the treasure\n")
choice1 = input(
    "You\'re at a crossroad, where do you want to go ? Type 'Left' or 'Right'.\n").lower()


if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of " +
                    "the lake. Type 'Wait' to wait for a boat. Type 'Swim' to swim across\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at an island unharmed. There is a house with 3 doors. One Red" +
                        " One Yellow and one Blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It is a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You entered a room full of beasts. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("you fell into a hole. Game Over")
