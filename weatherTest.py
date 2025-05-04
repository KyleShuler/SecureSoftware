import unittest 

from utils import validate_zip 

from weather import get_weather_forecast 

 

class TestWeatherApp(unittest.TestCase): 

     

    def test_valid_zip(self): 

        self.assertTrue(validate_zip("12345")) 

     

    def test_invalid_zip_letters(self): 

        self.assertFalse(validate_zip("12abc")) 

     

    def test_invalid_zip_short(self): 

        self.assertFalse(validate_zip("1234")) 

 

    def test_get_weather_forecast_success(self): 

        result = get_weather_forecast("10001")  

        self.assertIsNotNone(result) 

 

    def test_get_weather_forecast_invalid_zip(self): 

        result = get_weather_forecast("00000")   

        self.assertIsNone(result) 

 

if __name__ == '__main__': 

    unittest.main() 

 

 