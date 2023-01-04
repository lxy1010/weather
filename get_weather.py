import requests
import bs4
import json


def get_weather():
    res = requests.get('http://t.weather.sojson.com/api/weather/city/101200901')
    res.raise_for_status()
    weather_dict = eval(bs4.BeautifulSoup(res.text, 'html.parser').text)    # dict

    with open('data/weatherdata.json', 'w', encoding='utf-8') as f:
        json.dump(weather_dict, f, indent=4)
