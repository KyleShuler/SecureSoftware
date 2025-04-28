import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from logger import logger

load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather_forecast(zip_code):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast",
            params={
                "zip": f"{zip_code},us",
                "units": "metric",
                "appid": api_key
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        city = data["city"]["name"]
        forecasts = data["list"]

        output = f"Weather forecast for {city}:\n\n"
        count = 0
        current_date = None

        for forecast in forecasts:
            dt_txt = forecast["dt_txt"]
            forecast_date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date()

            if forecast_date != current_date:
                current_date = forecast_date
                count += 1
                temp = forecast["main"]["temp"]
                description = forecast["weather"][0]["description"]

                formatted_date = forecast_date.strftime("%m-%d-%Y")
                output += f"Date: {formatted_date}\n"
                output += f"Temperature: {temp}°C\n"
                output += f"Weather: {description}\n"
                output += "-" * 20 + "\n"

            if count == 3:
                break

        # Save history
        save_history(zip_code, city)

        # Log the successful request
        logger.info(f"Retrieved weather for ZIP {zip_code}")

        return output

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")
        return None
    except KeyError as e:
        logger.error(f"Unexpected API response structure: {e}")
        return None

def save_history(zip_code, city):
    history_record = {
        "zip_code": zip_code,
        "city": city,
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open('history.json', 'a') as file:
            file.write(json.dumps(history_record) + "\n")
    except Exception as e:
        logger.error(f"Failed to save history: {e}")
