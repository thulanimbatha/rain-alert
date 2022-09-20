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

today_forecast = data["forecast"]["forecastday"][0]  # this is a list

forecast_hours = today_forecast["hour"]  # this is a list

for fs_hour in forecast_hours:
    if fs_hour["will_it_rain"] == 0: 
        pass
    elif fs_hour["will_it_rain"] == 1:
        print(f"Bring an umbrella at: {fs_hour['time']}")
        
