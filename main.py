import json
import pyinputplus as pyip
import sys
import pyttsx3
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

    return 0


def auto(default=True, noweadata_code='101200901', update=False):
    if default:
        try:
            update_weather(weather_data()['cityInfo']['citykey'])  # 获取最新数据
        except KeyError:
            print(f'WeatherData 未初始化, 请检查后重试.\n使用默认 CityCode: {noweadata_code} '
                  f'{weather_data()["cityInfo"]["parent"]} {weather_data()["cityInfo"]["city"]}.\n\n')
            update_weather('101200901')

    else:
        update_weather(ask_users_city_code())
    if not update:
        qaa_wealike()


def auto_plan():
    def sayit(*arg):
        ps = pyttsx3.init()
        for saying in arg:
            print(saying)
            ps.say(saying)
            ps.runAndWait()
            time.sleep(0.5)

    auto(update=True)
    weather = weather_data()
    parent = weather['cityInfo']['parent']
    city = weather['cityInfo']['city']
    date = weather['date']
    uptime = weather['cityInfo']['updateTime']
    data = weather['data']
    forecast = data['forecast']
    sayit(f"大家好, 欢迎收听本次的 天气预报. ",
          f"现在是北京时间 {time.strftime('%H时%M分%S秒')}. ",
          f"接下来播报的是 {parent} {city} {date[:4]}年{date[4:6]}月{date[6:8]}日 (最新{uptime[:2]}时 {uptime[3:5]}分) 实时天气.",
          f"湿度: {data['shidu']} ",
          f"pm2.5; {data['pm25']} ",
          f"pm10: {data['pm10']} ",
          f"空气质量指标: {data['quality']} ",
          f"温度: {data['wendu']} ",
          f"小贴士: {data['ganmao']}",
          f"接下来播报的是: 14天 天气预报.")
    for day in forecast:
        dates = day['ymd']
        sayit(f"{dates[:4]}年{dates[5:7]}月{dates[8:10]}日",
              f"天气: {day['type']}",
              f"当日最高: {day['high']}",
              f"当日最低: {day['low']}",
              f"日出: {day['sunrise']}",
              f"日落: {day['sunset']}",
              f"空气质量指数: {day['aqi']}",
              f"风向: {day['fx']}",
              f"风速: {day['fl']}",
              f"小贴士: {day['notice']}")


auto_plan()
