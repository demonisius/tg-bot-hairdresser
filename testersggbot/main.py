import logging
from random import randint

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
from aiogram.utils.callback_data import CallbackData
from aiogram_calendar import (
    simple_cal_callback,
    SimpleCalendar,
)

import db
from config import WorkWindow

ww1 = WorkWindow()

# Объект бота
bot = Bot(token="5685322861:AAEoKnTXVE_20NudE-RKo-CRCwcIVul9uyY")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

start_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
)

# Кнопки внизу
start_kb.row("Записаться на приём")

"""
CMD Команды
"""


# Команда начало бота, точка входа
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(
        "Записаться на приём: ", reply_markup=await SimpleCalendar().start_calendar()
    )


"""
CMD Команды
"""


# Обработка блокировки бота пользователем
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


@dp.message_handler(Text(equals=["Записаться на приём"], ignore_case=True))
async def nav_cal_handler(message: Message):
    await message.answer(
        "Пожалуйтса выберите дату визита: ",
        reply_markup=await SimpleCalendar().start_calendar(),
    )


@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(
        callback_query, callback_data
    )
    if selected:
        await callback_query.message.answer(
            f'Вы выбрали {date.strftime("%d/%m/%Y")}', reply_markup=start_kb
        )
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                text="Нажми меня", callback_data="send_work_time"
            )
        )
        # await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

        await callback_query.message.answer(
            "Теперь выберите время", reply_markup=keyboard
        )


# Генератов расписания времени

# Подмешали свои колл бэки
cb_work_time = CallbackData("work_time", "w_time")


@dp.callback_query_handler(text="send_work_time")
async def send_work_cal_handler(call: types.CallbackQuery):  # (message: Message):
    # await call.message.answer("Пожалуйтса выберите время визита: ")

    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=False, row_width=6)
    counter = 0
    for value in ww1.work_hours_graf_1[0:-1]:
        button_inl_work_clock1 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter],
            # callback_data=ww1.work_hours_graf_1[counter],
            callback_data=cb_work_time.new(w_time=str(ww1.work_hours_graf_1[counter])),
        )
        button_inl_work_clock2 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 1],
            # callback_data=ww1.work_hours_graf_1[counter + 1],
            callback_data=cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 1])
            ),
        )
        button_inl_work_clock3 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 2],
            # callback_data=ww1.work_hours_graf_1[counter + 2],
            callback_data=cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 2])
            ),
        )
        button_inl_work_clock4 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 3],
            # callback_data=ww1.work_hours_graf_1[counter + 3],
            callback_data=cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 3])
            ),
        )
        button_inl_work_clock5 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 4],
            # callback_data=ww1.work_hours_graf_1[counter + 4],
            callback_data=cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 4])
            ),
        )
        button_inl_work_clock6 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 5],
            # callback_data=ww1.work_hours_graf_1[counter + 5],
            callback_data=cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 5])
            ),
        )
        menu_kb_inl.add(
            button_inl_work_clock1,
            button_inl_work_clock2,
            button_inl_work_clock3,
            button_inl_work_clock4,
            button_inl_work_clock5,
            button_inl_work_clock6,
        )
        counter += 6
        if counter == 24:
            break
    await call.message.delete_reply_markup()
    await call.message.answer("Выберите время: ", reply_markup=menu_kb_inl)


# Обработка нажатий кнопок с рабочим окном
@dp.callback_query_handler(cb_work_time.filter())
async def callbacks_work_time(call: types.CallbackQuery, callback_data: dict):
    # Обработка нажатий кнопок
    w_time = callback_data["w_time"]
    """
    Проверяем коллбэк с кнопки на пустую строку
    """
    if not w_time == " ":
        # print(w_time)
        # Удаляет клавитуру
        await call.message.delete_reply_markup()
        await call.message.answer("Вы записаны на " + str(w_time))


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
