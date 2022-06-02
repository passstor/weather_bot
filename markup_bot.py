from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_all = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новини")
        ],
        [
            KeyboardButton(text="Погода")
        ]
    ],
    resize_keyboard=True
)
markup_y_n = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="так")
        ],
        [
            KeyboardButton(text="ні")
        ]
    ],
    resize_keyboard=True
)
markup_news = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новини за запитом")
        ],
        [
            KeyboardButton(text="Звіт всіх новин за запитом")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup_news_next_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Наступна новина")
        ],
        [
            KeyboardButton(text="Минула новина")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода зараз")
        ],
        [
            KeyboardButton(text="Прогноз погоди")
        ],
        [
            KeyboardButton(text="Відправити звіт")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup_zvit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода зараз")
        ],
        [
            KeyboardButton(text="Прогноз погоди")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

markup_first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода зараз")
        ],
        [
            KeyboardButton(text="Прогноз погоди")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода зараз")
        ],
        [
            KeyboardButton(text="Прогноз погоди")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup_6 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погода зараз")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
markup_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)

markup_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прогноз погоди")
        ],
        [
            KeyboardButton(text="Відправити звіт")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)