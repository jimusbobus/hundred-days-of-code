# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
#
# print(format_name("TeST", "testER"))

def is_leap(_year):
    """calculate if the year provided was a leap year"""
    if _year % 4 == 0:
        if _year % 100 == 0:
            if _year % 400 == 0:
                print("Leap year")
                return True
            else:
                print("Not leap year")
                return False
        else:
            print("Leap year")
            return True
    else:
        print("Not leap year")
        return False


# TODO: Add more code here 👇
def days_in_month(_year, _month):
    """Locate the number of days in a month given a specific year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(_year):
        month_days[1] = 29
    # print(month_days)
    return month_days[_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("# Enter a year: "))
month = int(input(" # Enter a month: "))
days = days_in_month(year, month)
print(days)
