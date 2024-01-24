import os

import requests
from twilio.rest import Client
import smtplib

app_key = os.environ.get('app_key')
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
MY_PHONE = os.environ.get('MY_PHONE')
FROM_NUMBER = os.environ.get('FROM_NUMBER')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')

end_point = "https://api.openweathermap.org/data/2.5/forecast"

Latitude = 42.492603
longitude = 26.501442

weather_params = {
    "lat": "42.492603",
    "lon": "26.501442",
    "appid": app_key,
    "cnt": 4,
}
response = requests.get(end_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()
is_raining = False
for hours_data in range(0, 4):
    daily_code = weather_data['list'][hours_data]['weather'][0]['id']
    if daily_code < 700:
        is_raining = True

if is_raining:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"ste vali")
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=FROM_NUMBER,
        to=MY_PHONE,
        body="it won't rain",
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"nqma da vali")
