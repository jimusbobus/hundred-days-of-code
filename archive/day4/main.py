# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# # names_string contains the input values provided.
# # The code above converts the input into an array seperating
# # each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
#
# import random
#
# name_count = len(names)
#
# random_name = random.randint(0, name_count)
#
# print(f"{names[random_name]} is going to buy the meal today!")

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "️⬜️", "️⬜️"]
line3 = ["⬜️", "️⬜️", "️⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

my_coordinates_dict = {
    '1': 0,
    '2': 1,
    '3': 2,
    'a': 0,
    'b': 1,
    'c': 2
}

x_coordinate = position[0].lower()
y_coordinate = position[1].lower()

map[my_coordinates_dict[y_coordinate]][my_coordinates_dict[x_coordinate]] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
