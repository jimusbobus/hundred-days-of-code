import random
import datetime as dt
import smtplib

with open('quotes.txt', mode='r') as _file:
    all_quotes = [line.strip() for line in _file.readlines()]

random_quote = random.choice(all_quotes)
print(random_quote)

weekday = dt.datetime.now().weekday()
print(weekday)

if weekday == 1:
    my_email = "jimusbobus@gmail.com"
    pwd = "fqlt fhjb pqae sjjc"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jimusbobus@hotmail.com",
            msg=f"Subject:Happy Monday!!\n\n{random_quote}")
