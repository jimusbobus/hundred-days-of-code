# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
#
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Munich"],
#         "total_visits": 24
#     }
# }
#
# travel_log_list = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Munich"],
#         "total_visits": 24
#     },
# ]

country = input("Add country name: ")
visits = int(input("Number of visits: "))
list_of_cities = eval(input("create list from formatted string: "))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(_country, _visits, _list_of_cities):
    travel_log.append({
        "country": _country,
        "visits": _visits,
        "cities": _list_of_cities
    })


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
