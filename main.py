import requests
from twilio.rest import Client

api_key = "b68c788d8147467a8ff212807221509"
account_sid ="ACfa486f58e390aaf8fdb12578a32fd640"   #Twilio account details
auth_token = "5c4bfa87d74f879c4e903769bfa328fa"     #Twilio account details

parameters = {
    "key": api_key,
    "q" : "Johannesburg, South Africa",
    "days" : 7,
    "aqi" : "no",
    "alerts" : "no",
}

response = requests.get("http://api.weatherapi.com/v1/forecast.json", params=parameters)
response.raise_for_status()

data = response.json()

today_forecast = data["forecast"]["forecastday"][0]  # this is a list

forecast_hours = today_forecast["hour"][:12]  # slice list to only include first 12 elements

will_it_rain = False

for fs_hour in forecast_hours:
    if fs_hour["will_it_rain"] == 0: 
        will_it_rain = False
        pass
    elif fs_hour["will_it_rain"] == 1:
        will_it_rain = True
        print(f"Bring an umbrella at: {fs_hour['time']}")

if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="It's going to rain today, carry and umbrella...ella...ella...eh",
                                    from_="+16292763317",
                                    to="+27834158673"
                                    )

    print(message.status)
