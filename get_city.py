import json
import openpyxl as opxl


def get_city():
    wb = opxl.load_workbook('MR.WU.xlsx')
    sheet = wb['Sheet1']
    sheet_data = {}

    for row in range(2, sheet.max_row + 1):
        province = sheet[f'E{str(row)}'].value
        city = sheet[f'D{str(row)}'].value
        citycode = sheet[f'B{str(row)}'].value

        sheet_data.setdefault(province, {})
        sheet_data[province].setdefault(city, citycode)

    with open('citydata.json', 'w', encoding='utf-8') as f:
        json.dump(sheet_data, f, indent=4)
