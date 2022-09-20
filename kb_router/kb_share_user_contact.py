from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Отправить свой контакт ☎️", request_contact=True)
)
