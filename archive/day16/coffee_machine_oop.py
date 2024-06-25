from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()

menu = Menu()

mm = MoneyMachine()

QUARTERS = "quarters"
DIMES = "dimes"
NICKLES = "nickles"
PENNIES = "pennies"


def insert_coins():
    quarters = int(input(f"How many {QUARTERS}?: "))
    dimes = int(input(f"How many {DIMES}?: "))
    nickles = int(input(f"How many {NICKLES}?: "))
    pennies = int(input(f"How many {PENNIES}?: "))

    _total = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01), 2)
    print(f"DEBUG: total of ${_total} inserted.")
    return _total


machine_on = True
while machine_on:
    order_name = input(f"What would you like? ({menu.get_items()}): ")

    drinks = menu.get_items().split("/")[:-1]

    if order_name == 'off':
        machine_on = False
    elif order_name == 'report':
        print(coffeeMaker.report())
    elif order_name in drinks:
        drink = menu.find_drink(order_name)
        if coffeeMaker.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
    else:
        print(f"Selection {order_name} is not recognised.")
