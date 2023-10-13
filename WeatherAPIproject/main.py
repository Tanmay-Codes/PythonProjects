import requests
parameters = {
    "lat": "25.426359",
    "lon": "81.829613",
    "appid": "d4f60dde0b1088ab229b41bdf246ff10"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hour_data = data["hourly"][:12]

is_rainy = False

for items in hour_data:
    conditional_value = items["weather"][0]["id"]
    if int(conditional_value) < 700:
        is_rainy = True

if is_rainy:
    print("Bring your umbrella today please")
else:
    print("No Need to bring umbrella")