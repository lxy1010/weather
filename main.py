import requests
import bs4
import json
import openpyxl as opxl
import pyinputplus as pyip


res = requests.get('http://t.weather.sojson.com/api/weather/city/101200901')
res.raise_for_status()
weather_dict = eval(bs4.BeautifulSoup(res.text, 'html.parser').text)    # dict

# with open('package.json', 'w', encoding='utf-8') as f:
#     json.dump(weather_dict, f, indent=4)

with open('package.json', 'r', encoding='utf-8') as f:
    txt = json.load(f)

# wb = opxl.load_workbook('MR.WU.xlsx')
# sheet = wb['Sheet1']
# sheet_data = {}
#
# for row in range(2, sheet.max_row + 1):
#     province = sheet[f'E{str(row)}'].value
#     city = sheet[f'D{str(row)}'].value
#     citycode = sheet[f'B{str(row)}'].value
#
#     sheet_data.setdefault(province, {})
#     sheet_data[province].setdefault(city, citycode)
#
# with open('citydata.json', 'w', encoding='utf-8') as f:
#     json.dump(sheet_data, f, indent=4)

with open('citydata.json', 'r', encoding='utf-8') as f:
    city_data = json.load(f)


