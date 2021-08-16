# pylint: disable=missing-docstring
import sys
import requests
#import urllib.parse

BASE_URI = "https://www.metaweather.com"

def search_city(query='lon'):
    add_query = f"/api/location/search/?query={query}"
    get_city = requests.get(BASE_URI+add_query).json()
    if len(get_city) >= 1:
        return get_city[0]
    print("This city is not in the database, please try again")
    return None

def weather_forecast(woeid=44418):
    query_url=f'{BASE_URI}/api/location/{str(woeid)}'
    return requests.get(query_url).json()['consolidated_weather'][0:5]

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    #print(city)
    if city:
        city_woeid = city['woeid']
        weather_consolidated = weather_forecast(city_woeid)
        print("Here's the weather in London")
        for weather in weather_consolidated:
            max_temp = round(weather['max_temp'])
            print(f'{weather.get("applicable_date")} \
                {weather.get("weather_state_name")} {max_temp}°C')

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
