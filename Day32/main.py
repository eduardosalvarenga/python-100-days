# Create an automated "Happy Birthday" email sender with smtplib

import datetime as dt
import random
import pandas as pd
import smtplib

EMAIL = "XXXXXXX@gmail.com"
PASSWORD = "XXXXX"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays = pd.read_csv("birthdays.csv")
birth_dict = {(birthdays_row["month"], birthdays_row['day']): birthdays_row for (index, birthdays_row) in birthdays.iterrows()}

if today_tuple in birth_dict:
    letter = random.randint(1, 3)
    birthday_person = birth_dict[today_tuple]
    with open(f"letter_templates/letter_{letter}.txt") as data:
        content = data.read()
        final_letter = content.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday!\n\n{final_letter}")
