from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



on = True

while on:
    # current_resources = Menu()
    menu_items = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
  
    user_input = input(
        f"What coffee would you like? {menu_items.get_items()}: ")

    if user_input == "report":
        print(coffee_maker.report())
    elif user_input == "off":
        on = False
    else:
        coffee_type = menu_items.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(coffee_type):
            print("Please insert coins\n")
    #         quarters = float(input("How many quarters? "))
    #         dimes = float(input("How many dimes? "))
    #         nickels = float(input("how many nickels? "))
    #         pennies = float(input("How many pennies? "))

    #         check_cost(quarters, dimes, nickels, pennies, coffee)
