import json
import pyinputplus as pyip

from get_weather import get_weather
from get_city import get_city


def weather_data() -> dict:
    with open('data/weatherdata.json', 'r', encoding='utf-8') as f:
        txt = json.load(f)
    return txt


def city_data() -> dict:
    with open('data/citydata.json', 'r', encoding='utf-8') as f:
        citydata = json.load(f)
    return citydata


def update_weather():
    get_weather()


def update_city():
    get_city()


update_city()
update_weather()
