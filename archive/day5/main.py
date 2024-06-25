# fruits = ["apple", "peach", "pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " PIE")

# # Input a Python list of student heights
# student_heights = input("Input a Python list of student heights").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
#
# total_heights = 0
# student_count = 0
#
# for student_height in student_heights:
#     total_heights += student_height
#     student_count += 1
#
# average_height = round(total_heights / student_count)
#
# print(f"total height = {total_heights}")
# print(f"number of students = {student_count}")
# print(f"average height = {average_height}")

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# high_score = 0
# for score in student_scores:
#     if score > high_score:
#         high_score = score
#
# print(f"The highest score in the class is: {high_score}")

# total = 0
# for number in range(1, 101):
#     # print(number)
#     total += number
#
# print(total)

# target = int(input("Enter a number between 0 and 1000"))
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
#
# total = 0
# for number in range(total, target + 1, 2):
#     print(number)
#     total += number
#
# print(total)

# Your program should print each number from 1 to 100 in turn and include number 100.
#
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 100 + 1):
    if ((number % 3) == 0) and ((number % 5) == 0):
        print("FizzBuzz")
    elif (number % 5) == 0:
        print("Buzz")
    elif (number % 3) == 0:
        print("Fizz")
    else:
        print(number)
