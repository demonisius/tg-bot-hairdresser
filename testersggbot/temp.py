import telebot
from telebot import types
from telebot_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE
import datetime

bot = telebot.TeleBot("5685322861:AAEoKnTXVE_20NudE-RKo-CRCwcIVul9uyY")
calendar = Calendar(language=RUSSIAN_LANGUAGE)
calendar_1 = CallbackData("calendar_1", "action", "year", "month", "day")
now = datetime.datetime.now()


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    button1 = types.KeyboardButton("ЗАПИСЬ НА СЪЕМКУ")
    keyboard.add(button1)
    bot.send_message(
        message.chat.id,
        "Добро пожаловать, " + message.from_user.first_name + "!",
        reply_markup=keyboard,
    )


@bot.message_handler(content_types=["text"])
def call(message):
    # высвечиваем календарь при нажатии на кнопку ЗАПИСЬ НА СЪЕМКУ
    if message.text == "ЗАПИСЬ НА СЪЕМКУ":
        bot.send_message(
            message.chat.id,
            "Выберите дату",
            reply_markup=calendar.create_calendar(
                name=calendar_1.prefix, year=now.year, month=now.month
            ),
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1.prefix))
def callback_inline(call: types.CallbackQuery):
    name, action, year, month, day = call.data.split(calendar_1.sep)
    date = calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )

    if action == "DAY":
        bot.send_message(
            chat_id=call.from_user.id,
            text=f'Вы выбрали {date.strftime("%d.%m.%Y")}',
            reply_markup=types.ReplyKeyboardRemove(),
        )

    elif action == "CANCEL":
        bot.send_message(
            chat_id=call.from_user.id,
            text="Отмена",
            reply_markup=types.ReplyKeyboardRemove(),
        )
