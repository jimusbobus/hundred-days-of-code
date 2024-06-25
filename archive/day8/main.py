# # Review:
# # Create a function called greet().
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
#
#
# def greet(name, location):
#     print(f"Hello {name} from {location}")
#     print(f"sup {name}")
#     print(f"bye {name}")
#
#
# greet(name="jb", location="sheff")
# greet(location="gav", name="derby")

# Write your code below this line 👇
# import math
#
# def paint_calc(height, width, cover):
#     # print(height)
#     # print(width)
#     # print(coverage)
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall (m)"))
# test_w = int(input("Width of wall (m)"))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    # Since 1 is not a prime numer we start the loop at 2
    if number > 1:
        for count in range(2, number):
            # print(f"number={number}, count={count}")
            division = number / count
            # print(f"division={division}")
            if division % 1 == 0:
                is_prime = False
                # print(f"is_prime: {is_prime}")
    else:
        is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)