# Create a Coffee Machine

from menu import MENU
from menu import resources

MONEY_IN_THE_MACHINE = 0


def choice():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    return user_choice


def turn_off():
    quit()


def report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${MONEY_IN_THE_MACHINE}")


def m_resources(u_choice):
    ingredients = MENU[u_choice]['ingredients']

    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def p_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_coins = float(quarters + dimes + nickels + pennies)

    return total_coins


def transaction(u_choice, t_coins):
    global MONEY_IN_THE_MACHINE
    product_price = float(MENU[u_choice]['cost'])

    if product_price > t_coins:
        print("Sorry that's not enough money. Money refunded.")
    else:
        MONEY_IN_THE_MACHINE += product_price
        change = round(t_coins - product_price, 2)
        print(f"Here is ${change} dollars in change.")
        return True


def coffee():
    global MONEY_IN_THE_MACHINE
    f_choice = choice()
    if f_choice == 'off':
        turn_off()
    elif f_choice == 'report':
        report()
    else:
        f_resources = m_resources(f_choice)
        if f_resources:
            f_transaction = transaction(u_choice=f_choice, t_coins=p_coins())

            if f_transaction:
                ingredients = MENU[f_choice]['ingredients']
                resources['water'] -= ingredients['water']
                resources['coffee'] -= ingredients['coffee']
                MONEY_IN_THE_MACHINE += MENU[f_choice]['cost']
                if f_choice != 'espresso':
                    resources['milk'] -= ingredients['milk']

                print(f"Here is your {f_choice} ☕. Enjoy!")


order_finished = True
while order_finished:
    coffee()
