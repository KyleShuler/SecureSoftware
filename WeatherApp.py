import requests
import json
from datetime import datetime

# Enter zip code
zip_code = input("Enter ZIP code: ")


api_key = "56b253894318ce37e0088b106b095b76"

# Makeing the request
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?zip={zip_code},us&units=metric&appid={api_key}"
)


if response.status_code == 200:
    data = response.json()

    # city name
    city = data["city"]["name"]
    print(f"Weather forecast for {city}:\n")

    
    forecasts = data["list"]
    count = 0
    current_date = None


    for forecast in forecasts:
        # Get the date and time
        dt_txt = forecast["dt_txt"]
        forecast_date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date()

        
        if forecast_date != current_date:
            current_date = forecast_date
            count += 1
            temp = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]

            formatted_date = forecast_date.strftime("%m-%d-%Y")

            print(f"Date: {formatted_date}")
            print(f"Temperature: {temp}°C")
            print(f"Weather: {description}")
            print("-" * 20)

        # Stop after 3 days
        if count == 3:
            break
else:
    print(f"Error: {response.status_code}, Unable to fetch weather data.")
