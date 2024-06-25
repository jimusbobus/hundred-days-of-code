# # import csv
# #
# # temps = []
# #
# # with open('weather_data.csv', mode='r') as _file:
# #     data = csv.reader(_file)
# #     for row in data:
# #         print(row)
# #         if row[1] != "temp":
# #             temps.append(int(row[1]))
# #
# #
# # print(temps)
#
# import pandas
#
#
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9 / 5) + 32
#
#
# data = pandas.read_csv("./weather_data.csv")
#
# print(data)
#
# tmp_list = data['temp'].to_list()
# print(f"Mean: {data['temp'].mean()}")
# print(f"Max: {data['temp'].max()}")
#
# print(f"How Many Sunny: {data.condition.value_counts().get('Sunny')}")
#
#
# c = data[data.temp == data.temp.max()].temp
# print(f"temp: {celsius_to_fahrenheit(c)}")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data.columns.tolist())

# count squirrel colours

fur_count = data['Primary Fur Color'].value_counts()
print(fur_count)

fur = pandas.DataFrame(fur_count)
fur.to_csv("fur.csv")
