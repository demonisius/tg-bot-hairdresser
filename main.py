"""
TODO
Записаться на приём готово

Перевести на русский каленарь

Выборка из ДБ тдля генерации календаря

Пожалуйтса выберите дату визита: готово

Выборка из ДБ тдля генерации календаря

Пожалуйтса выберите время визита: готово

Взять контакт готово

Постать контакт,дату и время Админу

503415978 375296347998 SerggTech
5728236318 375291720006 Инга
"""


import logging

from aiogram import Bot, Dispatcher, types

from aiogram.dispatcher.filters import Text
from aiogram.types import (
    Message,
    CallbackQuery,
    ParseMode,
)
from aiogram.utils import executor
from aiogram.utils.exceptions import BotBlocked
from aiogram_calendar import (
    simple_cal_callback,
    SimpleCalendar,
)

import cb_custom
import config
import msg
import kb_router
from kb_router import kb_start, kb_inl_cmd_start, kb_inl_w_time, kb_share_user_contact

# Объект бота
bot = Bot(token="5685322861:AAEoKnTXVE_20NudE-RKo-CRCwcIVul9uyY")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

userSelectData = []
ww1 = config.WorkWindow()
db = config.db_conf.ClassForDB()

# Обработка блокировки бота пользователем
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


""" CMD Команды """


# Команда начало бота, точка входа
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    with open("img/hair-people-logo.png", "rb") as photo:
        await message.answer_photo(
            photo=photo, reply_markup=kb_router.kb_inl_cmd_start.kb_inl
        )
        # await message.answer("Записаться на приём: ", reply_markup=await SimpleCalendar().start_calendar())


@dp.message_handler(commands="db_table_creat")
async def cmd_admin_creat(message: types.Message):
    await message.answer("Таблицы DB созданы")
    db.table_creat_users_profile()
    db.table_creat_admin_profile()
    db.table_creat_tg_bot_users_recording()


""" CMD Команды """


# Обработка кнопок статового меню
@dp.callback_query_handler(Text(startswith="kbMenuStart_"))
async def callbacks_num(call: types.CallbackQuery):
    # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
    action = call.data.split("_")[1]
    match action:
        case "services":
            await call.message.answer(msg.msg_services, parse_mode=ParseMode.HTML)
            await call.message.delete_reply_markup()
            await call.message.answer(
                text="Назад", reply_markup=kb_router.kb_inl_cmd_start.kb_inl_back
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case "masters":
            await call.message.answer(msg.msg_masters, parse_mode=ParseMode.HTML)
            await call.message.delete_reply_markup()
            await call.message.answer(
                text="Назад", reply_markup=kb_router.kb_inl_cmd_start.kb_inl_back
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case "contacts":
            await call.message.answer(msg.msg_contacts, parse_mode=ParseMode.HTML)
            await call.message.delete_reply_markup()
            await call.message.answer(
                text="Назад", reply_markup=kb_router.kb_inl_cmd_start.kb_inl_back
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case "consult":
            await call.message.answer(msg.msg_consult, parse_mode=ParseMode.HTML)
            await call.message.delete_reply_markup()
            await call.message.answer(
                text="Назад", reply_markup=kb_router.kb_inl_cmd_start.kb_inl_back
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case "sign":
            await call.message.answer(
                "Записаться",
                reply_markup=await SimpleCalendar().start_calendar(),
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case "back":
            await call.message.delete_reply_markup()
            await call.message.answer(
                text="Назад", reply_markup=kb_router.kb_inl_cmd_start.kb_inl
            )
            # Не забываем отчитаться о получении колбэка
            await call.answer()

        case _:
            # Не забываем отчитаться о получении колбэка
            await call.answer()


""" Start menu """


@dp.message_handler(Text(equals=["Записаться"], ignore_case=True))
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
            f'Вы выбрали {date.strftime("%d/%m/%Y")}',
            reply_markup=kb_router.kb_start.kb,
        )

        # await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

        await callback_query.message.answer(
            "Пожалуйтса выберите время визита:",
            reply_markup=kb_router.kb_inl_w_time.kb_inl,
        )
        userSelectData.insert(0, date.strftime("%d-%m-%Y"))


# Генератов расписания времени


@dp.callback_query_handler(text="send_work_time")
async def send_work_cal_handler(call: types.CallbackQuery):  # (message: Message):
    # await call.message.answer("Пожалуйтса выберите время визита: ")

    kb_inl_work_clock = types.InlineKeyboardMarkup(resize_keyboard=False, row_width=6)
    counter = 0
    for value in ww1.work_hours_graf_1[0:-1]:
        button_inl_work_clock1 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter],
            # callback_data=ww1.work_hours_graf_1[counter],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter])
            ),
        )
        button_inl_work_clock2 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 1],
            # callback_data=ww1.work_hours_graf_1[counter + 1],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 1])
            ),
        )
        button_inl_work_clock3 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 2],
            # callback_data=ww1.work_hours_graf_1[counter + 2],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 2])
            ),
        )
        button_inl_work_clock4 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 3],
            # callback_data=ww1.work_hours_graf_1[counter + 3],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 3])
            ),
        )
        button_inl_work_clock5 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 4],
            # callback_data=ww1.work_hours_graf_1[counter + 4],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 4])
            ),
        )
        button_inl_work_clock6 = types.InlineKeyboardButton(
            text=ww1.work_hours_graf_1[counter + 5],
            # callback_data=ww1.work_hours_graf_1[counter + 5],
            callback_data=cb_custom.cb_work_time.new(
                w_time=str(ww1.work_hours_graf_1[counter + 5])
            ),
        )
        kb_inl_work_clock.add(
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
    await call.message.delete_reply_markup()  # Удаляем кнопки
    await call.message.answer("Выберите время: ", reply_markup=kb_inl_work_clock)
    await call.answer()


# Обработка нажатий кнопок с рабочим окном
@dp.callback_query_handler(cb_custom.cb_work_time.filter())
async def callbacks_work_time(call: types.CallbackQuery, callback_data: dict):
    # Обработка нажатий кнопок
    w_time = callback_data["w_time"]
    """ Проверяем коллбэк с кнопки на пустую строку """
    if not w_time == " ":
        # print(w_time)

        await call.message.delete_reply_markup()  # Удаляет клавитуру
        await call.message.edit_text("Вы записаны на " + str(w_time))
        await call.message.answer(
            "Отправьте свой контакт для связи ",
            reply_markup=kb_router.kb_share_user_contact.kb,
        )
        userSelectData.insert(1, str(w_time))
        await call.answer()

    await call.answer()


# Обработка высланого контакта
@dp.message_handler(content_types=[types.ContentType.CONTACT])
async def msg_handler_to_contact(message: Message):
    await message.answer(
        "Спасибо, " "Мастер свяжется с вами " "В ближайщее время",
        reply_markup=kb_router.kb_start.kb,
    )
    user_select_date = str(userSelectData[0])
    user_select_time = str(userSelectData[1])

    user_select_date = user_select_date.split("-")
    user_select_time = user_select_time.split("-")

    print(
        user_select_date[0],
        user_select_date[1],
        user_select_date[2],
        user_select_time[0],
        user_select_time[1]
        # message.contact.user_id,
        # message.from_user.username,
        # message.contact.first_name,
        # message.contact.last_name,
        # message.contact.phone_number,
        # message.contact.vcard,
        # message.contact.__annotations__,
        # message.__annotations__
    )

    db.table_insert_to_users_profile(
        message.contact.user_id,
        message.contact.phone_number,
        message.from_user.username,
        message.contact.first_name,
        message.contact.last_name,
    )
    db.table_insert_to_tg_bot_users_recording(
        message.contact.user_id,
        message.contact.phone_number,
        message.from_user.username,
        message.contact.first_name,
        message.contact.last_name,
        str(
            user_select_date[0] + ":" + user_select_date[1] + ":" + user_select_date[2]
        ),
        str(user_select_time[0] + ":" + user_select_time[1]),
    )


@dp.message_handler(content_types=[types.ContentType.TEXT])
async def msg_text_contact(message: Message):
    print(
        message.text
        # message.contact.vcard,
        # message.contact.__annotations__,
        # message.__annotations__
    )


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
