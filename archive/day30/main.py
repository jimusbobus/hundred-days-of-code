# fruits = eval(input('Fruits'))
#
#
# # 🚨 Do not change the code above
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print('Fruit pie')
#
#
# #  🚨 Do not change the code below
# make_pie(4)

# # eval() function will create a list of dictionaries using the input
# facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1},
#                   {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Comments': 1, 'Shares': 1},
#                   {'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
# print(total_likes)
