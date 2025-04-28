from utils import validate_zip 

from weather import get_weather_forecast 

from logger import logger 

 

def main(): 

    zip_code = input("Enter ZIP code: ") 

    if not validate_zip(zip_code): 
        print("Invalid ZIP code. Please enter a 5-digit number.") 
        return 

 

    forecast = get_weather_forecast(zip_code) 

    if forecast: 
        print(forecast) 

    else: 
        print("Failed to retrieve weather data. Please try again later.") 

 

if __name__ == "__main__": 
    main() 

 

 