print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


def count_true(name):
    name_t = name.upper().count("T")
    name_r = name.upper().count("R")
    name_u = name.upper().count("U")
    name_e = name.upper().count("E")
    return str(name_t + name_r + name_u + name_e)


def count_love(name):
    name_l = name.upper().count("L")
    name_o = name.upper().count("O")
    name_v = name.upper().count("V")
    name_e = name.upper().count("E")
    return str(name_l + name_o + name_v + name_e)


score = count_true(name1 + name2) + count_love(name1 + name2)

# print(score)

if (int(score) < 10) or (int(score) > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (int(score) < 50) and (int(score) > 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

