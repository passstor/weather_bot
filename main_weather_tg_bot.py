import requests
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from aiogram.types import  ReplyKeyboardRemove

from markup_bot import markup_all, markup, markup_news, markup_first, markup_y_n, markup_news_next_back, markup_6, \
    markup_2
from news import news
from clas import City
from excel import excell, excell_more_days,excell_news
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())





@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Напиши мені назву міста і я відправлю тобі погоду!\n", reply_markup=markup_all)


@dp.message_handler(text=["Відправити звіт"])
async def zvit(message: types.Message):
    await message.answer(f"Ваш звіт по місту", reply_markup=markup)
    await message.answer_document(open('Report.xlsx', 'rb'))
@dp.message_handler(text=["Новини"])
async def zvit(message: types.Message):
    await message.answer(f"Виберіть дію з новинами", reply_markup=markup_news)
@dp.message_handler(text=["Погода"])
async def zvit(message: types.Message):
    await message.answer(f"Виберіть дію з погодою", reply_markup=markup_first)

@dp.message_handler(text=["Погода зараз"])
async def start_command(message: types.Message):
    await message.answer("Напишіть місто", reply_markup=ReplyKeyboardRemove())
    await City.town_1.set()

@dp.message_handler(text=["Назад"])
async def start_command(message: types.Message):
    await message.answer("Виберіть дію", reply_markup=markup_all)
@dp.message_handler(text=["Прогноз погоди"])
async def start_command(message: types.Message):
    await message.answer("Напишіть місто", reply_markup=ReplyKeyboardRemove())

    await City.town_2.set()
@dp.message_handler(text=["Новини за запитом"])
async def start_command(message: types.Message):
    await message.answer("Напишіть запит для новин", reply_markup=ReplyKeyboardRemove())
    await City.new.set()
@dp.message_handler(text=["Звіт всіх новин за запитом"])
async def start_command(message: types.Message):
    await message.answer("Напишіть запит для новин", reply_markup=ReplyKeyboardRemove())
    await City.news_zvit.set()

@dp.message_handler(state=City.answer)
async def get_weather(message: types.Message, state: FSMContext):
    await state.update_data(answer=message.text)
    data = await state.get_data()
    answer=data.get("answer")
    if answer=="так":
        await state.update_data(news_state="Погода")
        data = await state.get_data()
        newc = data.get("news_state")
        a=(news((f'{newc}'), 1))
        if a==None:
            await state.reset_state()
            await message.answer("Змініть запит або мову запиту новин",reply_markup=ReplyKeyboardRemove())
            await City.news_zvit.set()
        else:
            excell_news((news((f'{newc}'), 1)), newc)
            await message.answer(f"Ваш звіт по темі {newc}", reply_markup=markup_all)
            await message.answer_document(open('Report_news.xlsx', 'rb'))
            await state.reset_state()
    else:
        await state.reset_state()
        await message.answer("Виберіть дію", reply_markup=markup_all)
@dp.message_handler(state=City.news_zvit)
async def get_weather(message: types.Message, state: FSMContext):
    try:
        if message.text=="Назад":
            await state.reset_state()
            await message.answer("Виберіть дію",reply_markup=markup_all)
        elif message.text=="Новини":
            await state.reset_state()
            await message.answer("Виберіть дію", reply_markup=markup_all)
        elif message.text=="Погода":
            await message.answer("Вам потрібні новини по погоді,виберіть \"так\" чи \"ні\"", reply_markup=markup_y_n)
            await City.answer.set()
        else:
            await state.update_data(news_state=message.text)
            data = await state.get_data()
            newc = data.get("news_state")
            a = (news((f'{newc}'), 1))
            if a == None:
                await state.reset_state()
                await message.answer("Змініть запит або мову запиту новин", reply_markup=ReplyKeyboardRemove())
                await City.news_zvit.set()
            else:
                excell_news((news((f'{newc}'), 1)), newc)
                await message.answer(f"Ваш звіт по темі {newc}")
                await message.answer_document(open('Report_news.xlsx', 'rb'), reply_markup=markup_all)
                await state.reset_state()
    except:
        await message.reply("\U00002699 Перевірте ваш запит \U00002699",
                            reply_markup=markup_all)
        await state.reset_state()


@dp.message_handler(state=City.new)
@dp.message_handler(state=City.iter)
@dp.message_handler(state=City.iterable)
async def get_weather(message: types.Message, state: FSMContext):

    if message.text=="Назад":
        await state.reset_state()
        await message.answer("Виберіть дію",reply_markup=markup_all)
    elif message.text=="Погода":
            await state.reset_state()
            await message.answer(f"Виберіть дію з погодою", reply_markup=markup_first)
    else:
        data = await state.get_data()
        i = data.get("iter")
        if message.text == "Наступна новина":
            i += 1
            await state.update_data(iter=i)
        elif message.text == "Минула новина":
            i -= 1
            await state.update_data(iter=i)
        else:
            await state.update_data(new=message.text)
        data = await state.get_data()
        i = data.get("iter")

        if message.text != "Минула новина" and message.text != "Наступна новина":
            await state.update_data(iter=0)
            data = await state.get_data()
            i = data.get("iter")
        try:
            new = data.get("new")
            a = (news((f'{new}'), 1))
            if a == None:
                await state.reset_state()
                await message.answer("Змініть запит або мову запиту новин", reply_markup=ReplyKeyboardRemove())
                await City.new.set()
            else:
                data = news(new, i)
                b = data["data"]
                lens = len(b["articles"])
                author = data["author"]
                title = data["title"]
                urltoimage = data["urltoimage"]
                description = data["description"]
                url = data["url"]
                if urltoimage == "None":
                    await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                         f"Автор статті: {author}\nЗаголовок: {title}\n"
                                         f"Опис статті: {description}\nUrl: {url}\n"
                                         f"Хорошого дня!", reply_markup=markup_news_next_back)
                else:
                    await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                         f"Автор статті: {author}\nЗаголовок: {title}\n"
                                         f"Опис статті: {description}\nUrl: {url}\nURLtoImage: {urltoimage}\n"
                                         f"Хорошого дня!", reply_markup=markup_news_next_back)
                await City.new.set()

        except:
            await message.reply("\U00002699 Перевірте ваш запит або в вас скінчилися новини \U00002699",
                                reply_markup=markup_all)
            await state.reset_state()


@dp.message_handler(state=City.zvit)
async def zvit(message: types.Message, state: FSMContext):
    await message.answer(f"Ваш звіт по місту", reply_markup=markup_first)
    await message.answer_document(open('Report.xlsx', 'rb'))

@dp.message_handler(state=City.town_2)
async def city_town(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city_1=city)
    if city == "Погода зараз":
        await message.answer("Введіть місто",reply_markup=ReplyKeyboardRemove())
        await state.reset_state()
        await City.town_1.set()
    elif city == "Відправити звіт":
        await state.reset_state()
    elif city == "Назад":
        await state.reset_state()
        await message.answer("Виберіть дію",reply_markup=markup_all)
    elif city == "/start":
        await state.reset_state()
        await message.reply("Привіт! Напиши мені назву міста і я відправлю тобі погоду!\n",
                            reply_markup=markup_all)
    else:
        await message.answer("На скільки днів вперед Ви хочете дізнатися погоду (до 5 днів)")
        await City.days.set()


@dp.message_handler(state=City.days)
async def city_town_days(message: types.Message, state: FSMContext):
    data = await state.get_data()
    city = data.get("city_1")
    days = message.text
    a=str(city)
    for i in a:
        if i==" ":
            lis = a.split(" ")
            if len(lis) > 1:
                for city in lis:
                    try:
                        r = requests.get(

                            f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
                        )
                        data = r.json()
                        excell_more_days(data, days)
                        if int(days) == 1:
                            days_name = "день"
                        elif int(days) in [2, 3, 4]:
                            days_name = "дня"
                        else:
                            days_name = "днів"
                        await message.answer(f"Звіт погоди за {days} {days_name},місто {city}", reply_markup=markup_6)
                        await message.answer_document(open('Report.xlsx', 'rb'))
                        await City.town_2.set()
                    except:
                        await message.answer("\U00002699 Перевірте назву міста або к-сть днів \U00002699",
                                             reply_markup=markup)
                        await state.reset_state()
                break
        elif i==",":
            lis = a.split(",")
            if len(lis) > 1:
                for city in lis:
                    try:
                        r = requests.get(

                            f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
                        )
                        data = r.json()
                        excell_more_days(data, days)
                        if int(days) == 1:
                            days_name = "день"
                        elif int(days) in [2, 3, 4]:
                            days_name = "дня"
                        else:
                            days_name = "днів"
                        await message.answer(f"Звіт погоди за {days} {days_name},місто {city}", reply_markup=markup_6)
                        await message.answer_document(open('Report.xlsx', 'rb'))
                        await City.town_2.set()
                    except:
                        await message.answer("\U00002699 Перевірте назву міста або к-сть днів \U00002699",
                                             reply_markup=markup)
                        await state.reset_state()
                break
    else:
        try:
            r = requests.get(

                f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={open_weather_token}&units=metric"
            )
            data = r.json()
            excell_more_days(data, days)
            if int(days) == 1:
                days_name = "день"
            elif int(days) in [2, 3, 4]:
                days_name = "дня"
            else:
                days_name = "днів"
            await message.answer(f"Звіт погоди за {days} {days_name}", reply_markup=markup_6)
            await message.answer_document(open('Report.xlsx', 'rb'))
            await message.answer(f"Напишіть місто або виберіть іншу ф-цію")
            await City.town_2.set()
        except:
            await message.answer("\U00002699 Перевірте назву міста або к-сть днів \U00002699", reply_markup=markup)
            await state.reset_state()


@dp.message_handler(state=City.town_1)
async def get_weather(message: types.Message, state: FSMContext):
    code_to_smile = {
        "Clear": "Ясно \U00002600","Clouds": "Хмарно \U00002601","Rain": "Дощ \U00002614","Drizzle": "Дрібний дощ \U00002614","Thunderstorm": "Гроза \U000026A1","Snow": "Сніг \U0001F328","Mist": "Туман \U0001F32B"
    }
    try:
        try:
            await state.update_data(city=message.text)
            data = await state.get_data()
            town_1 = data.get("city")
            if town_1 == "Прогноз погоди":
                await state.reset_state()
                await message.answer("Введіть місто",reply_markup=ReplyKeyboardRemove())
                await City.town_2.set()
            elif town_1 == "Відправити звіт":
                await state.reset_state()
                await City.zvit.set()
            elif town_1=="Назад":
                await state.reset_state()
                await message.answer("Ви вийшли назад",reply_markup=markup_all)
            elif town_1 == "/start":
                await state.reset_state()
                await message.reply("Привіт! Напиши мені назву міста і я відправлю тобі погоду!\n",
                                    reply_markup=markup_all)
            a=str(town_1)
            for i in a:
                if i==" ":
                    lis = a.split(" ")
                    if len(lis) > 1:
                        for city in lis:
                            r = requests.get(
                                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
                            )

                            data = r.json()
                            excell(data)
                            city = data["name"]
                            cur_weather = data["main"]["temp"]

                            weather_description = data["weather"][0]["main"]
                            if weather_description in code_to_smile:
                                wd = code_to_smile[weather_description]
                            else:
                                wd = "Не зрозуміла погода"

                            humidity = data["main"]["humidity"]
                            pressure = data["main"]["pressure"]
                            wind = data["wind"]["speed"]
                            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                            length_of_the_day = datetime.datetime.fromtimestamp(
                                data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                                data["sys"]["sunrise"])
                            await message.answer(f"Погода в місті: {city}\n***Станом на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\nТемпература: {cur_weather}C° {wd}\n"
                                                 f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\nТривалість дня: {length_of_the_day}\n"
                                                 f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n "
                                                 f"Хорошого дня!", reply_markup=markup_2)
                            await City.town_1.set()
                    break
                elif i==",":
                    lis = a.split(",")
                    if len(lis) > 1:
                        for city in lis:
                            r = requests.get(
                                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
                            )

                            data = r.json()
                            excell(data)
                            city = data["name"]
                            cur_weather = data["main"]["temp"]

                            weather_description = data["weather"][0]["main"]
                            if weather_description in code_to_smile:
                                wd = code_to_smile[weather_description]
                            else:
                                wd = "Не зрозуміла погода"

                            humidity = data["main"]["humidity"]
                            pressure = data["main"]["pressure"]
                            wind = data["wind"]["speed"]
                            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                            length_of_the_day = datetime.datetime.fromtimestamp(
                                data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                                data["sys"]["sunrise"])
                            await message.answer(f"Погода в місті: {city}\n***Станом на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\nТемпература: {cur_weather}C° {wd}\n"
                                                 f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\nТривалість дня: {length_of_the_day}\n"
                                                 f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n "
                                                 f"Хорошого дня!", reply_markup=markup_2)
                            await City.town_1.set()
                    break
            else:
                r = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={town_1}&appid={open_weather_token}&units=metric"
                )

                data = r.json()
                excell(data)
                city = data["name"]
                cur_weather = data["main"]["temp"]

                weather_description = data["weather"][0]["main"]
                if weather_description in code_to_smile:
                    wd = code_to_smile[weather_description]
                else:
                    wd = "Не зрозуміла погода"

                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]
                sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                length_of_the_day = datetime.datetime.fromtimestamp(
                    data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                    data["sys"]["sunrise"])
                await message.answer(f"Погода в місті: {city}\n***Станом на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\nТемпература: {cur_weather}C° {wd}\n"
                                                 f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\nТривалість дня: {length_of_the_day}\n"
                                                 f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n "
                                                 f"Хорошого дня!", reply_markup=markup_2)
                await City.town_1.set()




        except:

            await state.update_data(city=message.text)
            data = await state.get_data()
            town_1 = data.get("city")
            if town_1 == "Прогноз погоди":
                await state.reset_state()
                await City.town_2.set()
            elif town_1=="Назад":
                await state.reset_state()
                await message.answer("Виберіть дію")
            elif town_1 =="Відправити звіт":
                await state.reset_state()
                await message.answer(f"Ваш звіт по місту", reply_markup=markup_first)
                await message.answer_document(open('Report.xlsx', 'rb'))
            elif town_1=="/start":
                await state.reset_state()
            else:
                q = requests.get(
                    f"http://api.openweathermap.org/geo/1.0/direct?q={town_1}&limit=1&appid={open_weather_token}&units=metric"
                )
                data_1 = q.json()
                lat = data_1[0]['lat']
                lon = data_1[0]['lon']
                r = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}"
                    f"&appid={open_weather_token}&units=metric"
                )
                data = r.json()
                excell(data)

                city = data["name"]
                if city == "Podil":
                    city = "Kyiv"
                if city == "Pushcha-Vodytsya":
                    city = "Kyiv"
                cur_weather = data["main"]["temp"]

                weather_description = data["weather"][0]["main"]
                if weather_description in code_to_smile:
                    wd = code_to_smile[weather_description]
                else:
                    wd = "Не зрозуміла погода"

                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]
                sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                length_of_the_day = datetime.datetime.fromtimestamp(
                    data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                    data["sys"]["sunrise"])

                await message.answer(f"Погода в місті: {city}\n***Станом на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\nТемпература: {cur_weather}C° {wd}\n"
                                                 f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\nТривалість дня: {length_of_the_day}\n"
                                                 f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n "
                                                 f"Хорошого дня!", reply_markup=markup_2)
                await City.town_1.set()



    except:
        await state.update_data(city=message.text)
        data = await state.get_data()
        town_1 = data.get("city")
        if town_1 == "Прогноз погоди":
            await state.reset_state()
            await City.town_2.set()
        elif town_1=="Відправити звіт":
            await message.answer(f"Ваш звіт по місту", reply_markup=markup_first)
            await message.answer_document(open('Report.xlsx', 'rb'))
        elif town_1=="/start":
            await state.reset_state()
            await message.reply("Привіт! Виберіть дію!\n", reply_markup=markup_all)
        else:
            await message.reply("\U00002699 Перевірте назву міста \U00002699", reply_markup=markup_all)
            await state.reset_state()


if __name__ == '__main__':
    executor.start_polling(dp)
