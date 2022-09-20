import requests

api_key = "b68c788d8147467a8ff212807221509"

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

forecast_day = data["forecast"]["forecastday"]  # this is a list

first_day_forecast = forecast_day[0]["day"]

if first_day_forecast["daily_will_it_rain"] == 1:
    print("it will rain today")
elif first_day_forecast["daily_will_it_rain"] == 0:
    print("it will NOT rain")

# print(first_day_forecast)
