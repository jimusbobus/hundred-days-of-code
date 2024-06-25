# Tip calculator

print("Welcome to the tip calculator!\n")

total_bill = float(input("Enter the total bill in $.\n"))

tip_percentage = int(input("How much percentage tip would you like to give? (10, 12, 15)\n"))

party_size = int(input("How many people are sharing the bill.?\n"))

tip_percentage_as_decimal = tip_percentage / 100

tip_value = tip_percentage_as_decimal * total_bill

bill_tip_total = total_bill + tip_value

bill_share = round(bill_tip_total / party_size, 2)
bill_share2 = ""

print(f"The total tip was: ${tip_value}, each person should pay: ${bill_share}")
