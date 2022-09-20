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

print(data)
