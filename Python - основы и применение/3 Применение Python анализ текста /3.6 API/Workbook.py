# API

import pprint
import requests

class ApixuWeatherForecast:

    def __init__(self):
        self._city_cache = {}


    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = "http://api.apixu.com/v1/forecast.json?key=94224bc46fd34e7d90d150614191605&q={city}"
        print("Sending request...\n")
        data = requests.get(url).json()
        forecast_data = data["current"]
        forecast = []
        forecast.append({
            "date" : forecast_data["last_updated"],
            "high_temp" : forecast_data["temp_c"]
        })
        self._city_cache[city] = forecast
        return forecast

class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or ApixuWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    weather_forecast = ApixuWeatherForecast()
    city = 'Moscow'
    city_info = CityInfo(city, weather_forecast=weather_forecast)
    pprint.pprint(city_info.weather_forecast())

api_url = "http://api.apixu.com/v1/forecast.json"

params = {
    'key' : '94224bc46fd34e7d90d150614191605',
    'q' : 'Moscow'
}
res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers['Content-Type'])
print(res.json())

if __name__ == "__main__":
    _main()