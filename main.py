import json
import pyinputplus as pyip
import sys
import time

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


def update_weather(code):
    if not get_weather(code):
        print("运行终止.")
        sys.exit()


def update_city():
    get_city()


def ask_users_city_code() -> int:
    city = city_data()
    user_province = pyip.inputMenu(list(city.keys()), numbered=True, prompt='请输入您想查询的省: \n')
    user_city = pyip.inputMenu(list(city[user_province].keys()), numbered=True, prompt='\n请输入您想查询的市: \n')
    return city[user_province][user_city]


def qaa_wealike():
    def outyb(head_flag=False, sleep=0.0):
        if head_flag:
            time.sleep(sleep)
            print(f"{day['ymd']}  {day['week']}:\n\t", end='')
        else:
            print(f"\n{yb} 天气预报 ({weather['cityInfo']['parent']} "
                  f"{weather['cityInfo']['city']} {weather['cityInfo']['updateTime']}更新): \n\t", end='')
        print(f"-天气: {day['type']}\n\t"
              f"-当日最高: {day['high']}\n\t"
              f"-当日最低: {day['low']}\n\t"
              f"-日出: {day['sunrise']}\n\t"
              f"-日落: {day['sunset']}\n\t"
              f"-空气质量指数: {day['aqi']}\n\t"
              f"-风向: {day['fx']}\n\t"
              f"-风速: {day['fl']}\n\t"
              f"-小贴士: {day['notice']}\n")

    weather = weather_data()
    data = weather['data']

    cncode_uncode = {"当前": 'now', "预报": 'forecast'}

    print(f"天气查询 {weather['time']} {weather['cityInfo']['parent']} {weather['cityInfo']['city']} "
          f"(上一次更新 {weather['cityInfo']['updateTime']})")
    dy = pyip.inputMenu(list(cncode_uncode.keys()), numbered=True, prompt='\n您希望查询: \n')
    if cncode_uncode[dy] == 'now':
        print(f"\n最近一次天气"
              f"({weather['cityInfo']['parent']} {weather['cityInfo']['city']} {weather['cityInfo']['updateTime']}更新): "
              f"\n\t-湿度: {data['shidu']}\n\t"
              f"-pm2.5: {data['pm25']}\n\t"
              f"-pm10: {data['pm10']}\n\t"
              f"-空气质量指标: {data['quality']}\n\t"
              f"-温度: {data['wendu']}\n\t"
              f"-小贴士: {data['ganmao']}\n")
    else:
        forecast = data['forecast']
        all_day = [day['ymd'] + '  ' + day['week'] for day in forecast]
        yb = pyip.inputMenu(all_day + ['14天'], numbered=True, prompt='\n您希望查询: \n')
        if yb == '14天':
            print(f"\n14天 天气预报 ({weather['cityInfo']['parent']} "
                  f"{weather['cityInfo']['city']} {weather['cityInfo']['updateTime']}更新): \n\t")
            for day in forecast:
                outyb(True)
        for day in forecast:
            if yb == day['ymd'] + '  ' + day['week']:
                outyb()


def auto(default=True, noweadata_code='101200901'):
    if default:
        try:
            update_weather(weather_data()['cityInfo']['citykey'])    # 获取最新数据
        except KeyError:
            print(f'WeatherData 未初始化, 请检查后重试.\n使用默认 CityCode: {noweadata_code} '
                  f'{weather_data()["cityInfo"]["parent"]} {weather_data()["cityInfo"]["city"]}.\n\n')
            update_weather('101200901')

    else:
        update_weather(ask_users_city_code())
    qaa_wealike()


auto(True)
