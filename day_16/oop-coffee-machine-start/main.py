from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True

while on:
    menu_items = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    user_input = input(
        f"What coffee would you like? {menu_items.get_items()}: ")

    if user_input == "report":
        coffee_maker.report()
    elif user_input == "off":
        on = False
    else:
        coffee_type = menu_items.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(coffee_type):
            if money_machine.make_payment(coffee_type.cost):
                coffee_maker.make_coffee(coffee_type)
