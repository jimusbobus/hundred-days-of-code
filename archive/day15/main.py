# import helper
#
# WATER = "water"
# MILK = "milk"
# COFFEE = "coffee"
#
# QUARTERS = "quarters"
# DIMES = "dimes"
# NICKLES = "nickles"
# PENNIES = "pennies"
#
# coins = [QUARTERS, DIMES, NICKLES, PENNIES]
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def resources_report():
#     global resources
#     print(f"{WATER.title()}: {resources[WATER]}ml")
#     print(f"{MILK.title()}: {resources[MILK]}ml")
#     print(f"{COFFEE.title()}: {resources[COFFEE]}g")
#
#
# def has_enough_resources(_drink, _ingredients):
#     global resources
#     print(f"DEBUG: Coffee choice is {_drink}, has ingredients {_ingredients}")
#     if (MILK in _ingredients) and (_ingredients[MILK] > resources[MILK]):
#         print(f"There is not enough {MILK.title()}")
#         return False
#     elif (WATER in _ingredients) and (_ingredients[WATER] > resources[WATER]):
#         print(f"There is not enough {WATER.title()}")
#         return False
#     elif (COFFEE in _ingredients) and (_ingredients[COFFEE] > resources[COFFEE]):
#         print(f"There is not enough {COFFEE.title()}")
#         return False
#     else:
#         # print("DEBUG: sufficient ingredients.")
#         return True
#
#
# def insert_coins_calculate_total():
#     _q = int(input(f"How many {QUARTERS}?: "))
#     _d = int(input(f"How many {DIMES}?: "))
#     _n = int(input(f"How many {NICKLES}?: "))
#     _p = int(input(f"How many {PENNIES}?: "))
#
#     _total = round((_q * 0.25) + (_d * 0.1) + (_n * 0.05) + (_p * 0.01), 2)
#     print(f"DEBUG: total of ${_total} inserted.")
#     return _total
#
#
# def reduce_resources_by_ingredients(_ingredients):
#     if MILK in _ingredients:
#         resources[MILK] -= _ingredients[MILK]
#     if WATER in _ingredients:
#         resources[WATER] -= _ingredients[WATER]
#     if COFFEE in _ingredients:
#         resources[COFFEE] -= _ingredients[COFFEE]
#
#
# def dispense_drink(_inserted_total, _drink, _drink_cost, _ingredients):
#     global resources
#     # print(f"DEBUG: User provided ${_inserted_total}, wants {_drink.title()}, which costs ${_drink_cost}")
#     if _drink_cost > _inserted_total:
#         print(f"{_drink.title()} costs ${_drink_cost}, you only have ${_inserted_total}, coins returned.")
#         return
#     _change = round((_inserted_total - _drink_cost), 2)
#     if _change > 0:
#         print(f"Here is ${_change} in change.")
#     print(f"Here is your {_drink.title()}.")
#     reduce_resources_by_ingredients(_ingredients)
#
#
# def coffee_machine():
#     plugged_in = True
#     while plugged_in:
#         drinks = list(helper.MENU.keys())
#         choice = input(f"What would you like? {drinks}: ").lower()
#         if choice == 'report':
#             resources_report()
#         elif choice == 'off':
#             plugged_in = False
#         elif choice in drinks:
#             if has_enough_resources(choice, helper.MENU[choice]['ingredients']):
#                 inserted_total = insert_coins_calculate_total()
#                 dispense_drink(inserted_total, choice, helper.MENU[choice]['cost'], helper.MENU[choice]['ingredients'])
#         else:
#             print("Invalid choice, try again.")
#
#
# coffee_machine()
