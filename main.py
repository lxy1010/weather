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


def ask_users_city_code() -> dict:
    city = city_data()
    user_province = pyip.inputMenu(list(city.keys()), numbered=True, prompt='请输入您想查询的省: \n')
    user_city = pyip.inputMenu(list(city[user_province].keys()), numbered=True, prompt='\n请输入您想查询的市: \n')
    return {'city': user_city if user_province == user_city else user_province + user_city,
            'code': city[user_province][user_city]}


print(ask_users_city_code())
