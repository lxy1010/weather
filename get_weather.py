import requests
import bs4
import json


def get_weather(code: str) -> bool:
    res = requests.get(f'http://t.weather.sojson.com/api/weather/city/{code}')
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print("CityCode 无效, 请重试.")
        print(f"CityCode {code}")
        return False
    weather_dict = eval(bs4.BeautifulSoup(res.text, 'html.parser').text)    # dict

    with open('data/weatherdata.json', 'w', encoding='utf-8') as f:
        json.dump(weather_dict, f, indent=4)
    return True
