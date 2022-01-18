import time
import requests
from datetime import datetime
import smtplib

EMAIL = "XXXXXXX@gmail.com"
PASSWORD = "XXXXX"
MY_LAT = -27.596910
MY_LONG = -48.549580


def in_range():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()["iss_position"]

    longitude = float(iss_data["longitude"])
    latitude = float(iss_data["latitude"])

    if latitude + 5 >= MY_LAT >= longitude - 5 and latitude + 5 >= MY_LONG >= longitude - 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_data = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_data.raise_for_status()

    sun_data = sun_data.json()["results"]
    sunrise = int(sun_data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="test@gmail.com",
                            msg="Subject: Look up!!\n\nThe Iss is above you in the sky!")


while True:
    time.sleep(60)
    if in_range() and is_night():
        send_email()
