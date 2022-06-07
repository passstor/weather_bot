from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_all = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новини")
        ],
        [
            KeyboardButton(text="Погода")
        ],
        [
            KeyboardButton(text="До керування акаунтом")
        ]
    ],
    resize_keyboard=True
)
markup_acc = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Видалити акаунт")
        ],
        [
            KeyboardButton(text="Зареєструватися")
        ],
        [
            KeyboardButton(text="До розділів")
        ],
    ],
    resize_keyboard=True
)
markup_reg = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Зареєструватися")
        ]

    ],
    resize_keyboard=True
)
markup_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Зареєструватися")
        ],
        [
            KeyboardButton(text="Продовжити без реєстрації")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
        ]
    ],
    resize_keyboard=True
)
markup_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Відхилити")
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
        ],
        [
            KeyboardButton(text="До керування акаунтом")
        ]
    ],
    resize_keyboard=True
)