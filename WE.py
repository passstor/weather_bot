from datetime import datetime
from pprint import pprint

import openpyxl
import requests

from config import open_weather_token


def excell(data):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = "Місто"
    sheet['B1'] = "Температура"
    sheet['C1'] = "Опис погоди"
    sheet['D1'] = "Вологість"
    sheet['E1'] = "Тиск"
    sheet['G1'] = "Відчувається як"
    sheet['F1'] = "Вітер"
    sheet['H1'] = "Вітер"
    sheet['I1'] = "Вітер"
    sheet['J1'] = "Звіт зроблений"

    row = 2
    sheet[row][0].value = f'{data["name"]}'
    sheet[row][1].value = f'{data["main"]["temp"]} C°'
    sheet[row][2].value = data["weather"][0]["main"]
    sheet[row][3].value = f'{data["main"]["humidity"]} %'
    sheet[row][4].value = f'{data["main"]["pressure"]} мм.рт.ст"'
    sheet[row][5].value = f'{data["wind"]["speed"]} м/с'
    #sheet[row][6].value = f'{data["main"]["feels_like"]} C°'
    sheet[row][10].value = datetime.now().strftime('%Y-%m-%d %H:%M')
    row+=1
    book.save("Reports.xlsx")
    book.close()
#excell()
city="Київ"
q = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={open_weather_token}&units=metric"
)
data_1 = q.json()
lat = data_1[0]['lat']
lon = data_1[0]['lon']

def func_1():
    title = "Bimbas"
    description = "8 let"
    author = "Maksim"

    a = {
        "title": f'{title}',
        "description": f'{description}',
        "author": f'{author}'
    }
    return a
dic=func_1()
print(dic["description"])








