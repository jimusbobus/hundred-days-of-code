############DEBUGGING#####################

# # # Describe Problem - print line when i equals 20
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# # Reproduce the Bug
# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, len(dice_imgs))
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if (year > 1980) and (year <= 1994):
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is Your Friend
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"DEBUG: pages = {pages}, words = {word_per_page}, total = {total_words}")
# print(total_words)

# Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# # Which year do you want to check?
# year = int(input("Enter year: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


target = int(input("Enter a number: "))
for number in range(1, target + 1):
    print(f"DEBUG: number = {number}, target = {target}, n % 3 = {number % 3}, n % 5 = {number % 5}")
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
