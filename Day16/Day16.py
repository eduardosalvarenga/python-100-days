# Use the files provided (coffee_maker, menu and money_machine)
# to create the same project from Day 15 (Coffee Machine) but using OOP (Object Oriented Programming)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    u_choice = input(f"What would you like? ({menu.get_items()})?: ")

    if u_choice == 'off':
        is_on = False
    elif u_choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        user_drink = menu.find_drink(u_choice)
        resources = coffee_machine.is_resource_sufficient(user_drink)

        if resources:
            payment = money_machine.make_payment(user_drink.cost)

            if payment:
                coffee_machine.make_coffee(user_drink)