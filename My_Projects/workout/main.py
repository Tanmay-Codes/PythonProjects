import requests
import datetime

today = datetime.date.today()
print(today)
APP_ID = '384052c2'
APP_KEY = 'd6f3fdae5a40eedf4a042ac8332dcd83'
API_END_POINT = 'https://trackapi.nutritionix.com'

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise_text = input('which exercise did you do today?')
parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 92,
    "height_cm": 176,
    "age": 28
}

response = requests.post(url=f"{API_END_POINT}/v2/natural/exercise", json=parameters, headers=header)
result = response.json()
sheety_end_point = 'https://api.sheety.co/bc578a326dfdd4a35fc8681527f7cb99/workout/workouts'

today_date = datetime.datetime
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheety_end_point, json=sheet_inputs)

    print(sheet_response.text)