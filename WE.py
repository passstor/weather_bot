from datetime import datetime
from pprint import pprint

from psycopg2.extras import RealDictCursor, execute_values
from validate_email import validate_email
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

# login = "nazar08032003@mail.com"
# is_valid = validate_email(login, verify=True)
# print(is_valid)
y=datetime.now().strftime('%Y')
m=datetime.now().strftime('%m')
d=datetime.now().strftime('%d')
a=datetime.now().strftime('%Y-%m-%d %H:%M')
print(a[0:4])#рік
print(a[5:7]) #місяць
print(a[8:10]) #день
print(a[11:13]) #година
print(a[14:16]) #хвилини
#print(y,m,d)




