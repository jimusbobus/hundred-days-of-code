# with open('./file1.txt', mode='r') as _file:
#     f1_int_list = [int(line.strip()) for line in _file.readlines()]
#
# with open('./file2.txt', mode='r') as _file:
#     f2_int_list = [int(line.strip()) for line in _file.readlines()]
#
#
# result = [i for i in f1_int_list if i in f2_int_list]
# # Write your code above 👆
# print(result)

# sentence = input("Enter Sentence.")
# # 🚨 Don't change code above 👆
# # Write your code below 👇
#
# result = {word: len(word) for word in sentence.split(' ')}
#
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# # 🚨 Don't change code above 👆
#
# # (temp_c * 9/5) + 32 = temp_f
#
#
#
# # Write your code 👇 below:
#
# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
#
#
# print(weather_f)

# import pandas
#
# student_dict = {
#     "student": ['a', 'b', 'd'],
#     "score": [56, 67, 78]
# }
#
# student_df = pandas.DataFrame(student_dict)
# print(student_df)
#
# students = {row.student for (index, row) in student_df.iterrows() if row.student == 'b'}
#
# print(students)