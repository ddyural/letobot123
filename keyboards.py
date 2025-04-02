from operator import truediv

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IT лагеря👀"),
            KeyboardButton(text="языковые лагеря👀")
        ],
        [
            KeyboardButton(text="спортивные  лагеря👀"),
            KeyboardButton(text="кулинарные  лагеря👀")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="⬇Выберите действие⬇"
)



links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="NUUM", url="https://nuum.ru/channel/leotop" ),
            InlineKeyboardButton(text="Telegram", url="https://nuum.ru/channel/leotop")
        ]
    ]
)

#KeyboardButton(text="Назад❎"),