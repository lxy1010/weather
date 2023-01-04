import requests
import bs4
import json


res = requests.get('http://t.weather.sojson.com/api/weather/city/101200901')
res.raise_for_status()
text = eval(bs4.BeautifulSoup(res.text, 'html.parser').text)

with open('package.json', 'w', encoding='utf-8') as f:
    json.dump(text, f, indent=4)

print(text['data']['shidu'])
