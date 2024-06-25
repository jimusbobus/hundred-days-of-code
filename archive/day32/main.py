import pandas
import datetime as dt
import random
import smtplib

BIRTHDAYS_FILE = "birthdays.csv"
# ----------- Extra Hard Starting Project -----------

# 1. Update the birthdays.csv
try:
    all_birthdays_df = pandas.read_csv(BIRTHDAYS_FILE)
except FileNotFoundError:
    birthdays = []
else:
    birthdays = all_birthdays_df.to_dict(orient="records")

print(f"DEBUG: {birthdays[0]}")
print(f"DEBUG: Year: {birthdays[0]['year']}")
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now().today()

birthdays_today = [birthday for birthday in birthdays if
                   (today.day == birthday['day']) and (today.month == birthday['month'])]

print(f"DEBUG: Today's Birthdays: {birthdays_today}")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
letters = ["./letter_templates/letter_1.txt"]
random_letter = random.choice(letters)
# Read the file and replace the string
with open(random_letter, 'r') as file:
    email_message = file.read()
# Replace the target string with the new string
[birthday.update({'message': email_message.replace("[NAME]", birthday['name'])}) for birthday in birthdays_today]
print(birthdays_today)

# 4. Send the letter generated in step 3 to that person's email address.

my_email = "jimusbobus@gmail.com"
pwd = "fqlt fhjb pqae sjjc"

for birthday in birthdays_today:
    print(f"DEBUG: Sending to: {birthday['name']} @:{birthday['email']}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday['email'],
            msg=f"Subject:Happy Birthday!!\n\n{birthday['message']}")
