from menu import MENU, resources


def check_resources(coffee):
    for ingredient, amount in coffee["ingredients"].items():
        if amount > current_resources[ingredient]:
            print(f"Sorry there isn't enough {ingredient}")
            return False
    return True

def check_cost(quarters, dimes, nickels, pennies, coffee):
    total_cash = (quarters * 0.25) + (dimes * 0.10) + (nickels *
                                                       0.05) + (pennies * 0.01)
    print(total_cash)
    if coffee["cost"] > total_cash:
        print("Sorry that's not enough money. Money refunded.")
    else:
        update_resources(coffee)
        perform_transaction(total_cash)

def update_resources(coffee):
    for ingredient, amount in coffee["ingredients"].items():
        current_resources[ingredient] -= amount

def perform_transaction(total_cash):
    balance = total_cash - coffee["cost"]
    balance = round(balance, 3)
    print(
        f"Here's your balance {balance} \nAnd here's your {coffee_type}. Enjoy!"
    )
    if "Money" in resources:
        resources["Money"] += coffee["cost"]
    else:
        resources["Money"] = coffee["cost"]


should_continue = True
while should_continue:
    current_resources = resources
    coffee_type = input("What coffee would you like? espresso/latte/cappuccino: ")

    if coffee_type == "report":
        for item, amount in current_resources.items():
            print(f"{item} : {amount}")
    elif coffee_type == "off":
        should_continue = False
    else:
        coffee = MENU[coffee_type]
        if check_resources(coffee):
            print("Please insert coins\n")
            quarters = float(input("How many quarters? "))
            dimes = float(input("How many dimes? "))
            nickels = float(input("how many nickels? "))
            pennies = float(input("How many pennies? "))

            check_cost(quarters,dimes,nickels,pennies, coffee)
