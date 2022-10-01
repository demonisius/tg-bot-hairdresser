"""
TODO Перевести на русский каленарь
TODO Выборка из ДБ для генерации календаря


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
import aiogram.utils.markdown as fmt
from aiogram.utils.exceptions import BotBlocked
from aiogram_calendar import (
    simple_cal_callback,
    SimpleCalendar,
)

import cb_custom
import config
import kb_router
import msg
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

""" Обработка ошибок бота """


# Обработка блокировки бота пользователем
@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True


""" Обработка ошибок бота """

""" CMD Команды """


# Команда начало бота, точка входа
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    with open("img/hair-people-logo.png", "rb") as photo:
        await message.answer_photo(
            photo=photo, reply_markup=kb_router.kb_inl_cmd_start.kb_inl
        )


""" Команды для админов """


# Команда для создания таблиц в базеданых
@dp.message_handler(commands="db_table_creat")
async def db_table_creat(message: types.Message):
    await message.answer("Таблицы DB созданы")
    db.creat_users_profile()
    db.creat_admin_profile()
    db.creat_tg_bot_users_recording()


"""Open record ---> Close record"""


# Команда для выборки открытых записей
@dp.message_handler(commands="users_open_recording")
async def users_open_recording(message: types.Message):
    if message.from_user.id in db.fetch_from_admin_profile():
        fetch = db.fetch_from_tg_bot_users_open_recording()
        kb_inl_status = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
        for val in fetch:
            button_inl_status_row = types.InlineKeyboardButton(
                text=str("Запись " + val[0] + " в " + val[1]),
                # callback_data=str(val[2]),
                callback_data=cb_custom.cb_open_recording.new(recording_id=val[2]),
            )
            kb_inl_status.insert(button_inl_status_row)
        await message.answer("Выборка открытых записей", reply_markup=kb_inl_status)
    else:
        await message.answer("Вы не являетесь администратором")


# Обработка нажатий кнопок для закрытия записей
@dp.callback_query_handler(cb_custom.cb_open_recording.filter())
async def callbacks_users_open_recording(
        call: types.CallbackQuery, callback_data: dict
):
    # Обработка нажатий кнопок
    recording_id = callback_data["recording_id"]
    """ Проверяем коллбэк с кнопки на пустую строку """
    if not recording_id == " ":
        # print(recording_id)
        db.update_from_tg_bot_users_open_recording(recording_id)
        # await call.message.delete_reply_markup()  # Удаляет клавитуру
        # await call.message.edit_text("Вы записаны на " + str(w_time))
        # await call.message.answer(
        #    "Отправьте свой контакт для связи ",
        #    reply_markup=kb_router.kb_share_user_contact.kb,
        # )
        # userSelectData.insert(1, str(w_time))
        await call.message.edit_text("Запись успешно отредактирована")
        await call.message.delete_reply_markup()  # Удаляет клавитуру
        await call.answer()

    await call.answer()


"""Open record ---> Close record"""


# Команда для выборки закрытых записей
@dp.message_handler(commands="users_close_recording")
async def users_close_recording(message: types.Message):
    if message.from_user.id in db.fetch_from_admin_profile():
        fetch = db.fetch_from_tg_bot_users_close_recording()
        kb_inl_status = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
        for val in fetch:
            button_inl_status_row = types.InlineKeyboardButton(
                text=str("Запись " + val[0] + " в " + val[1]),
                callback_data=str(val[0] + " " + val[1]),
            )
            kb_inl_status.insert(button_inl_status_row)
        await message.answer("Выборка закрытых записей", reply_markup=kb_inl_status)
    else:
        await message.answer("Вы не являетесь администратором")


# Команда для выборки всех записей
@dp.message_handler(commands="users_all_recording")
async def users_recording(message: types.Message):
    if message.from_user.id in db.fetch_from_admin_profile():
        fetch = db.fetch_from_tg_bot_users_all_recording()
        kb_inl_status = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
        for val in fetch:
            button_inl_status_row = types.InlineKeyboardButton(
                text=str("Запись " + val[0] + " в " + val[1]),
                callback_data=str(val[0] + " " + val[1]),
            )
            kb_inl_status.insert(button_inl_status_row)
        await message.answer("Выборка всех записей", reply_markup=kb_inl_status)
    else:
        await message.answer("Вы не являетесь администратором")


""" Команды для админов """

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
            f'Вы выбрали {date.strftime("%d.%m.%Y")}',
            reply_markup=kb_router.kb_start.kb,
        )

        # await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

        await callback_query.message.answer(
            "Пожалуйтса выберите время визита:",
            reply_markup=kb_router.kb_inl_w_time.kb_inl,
        )
        userSelectData.insert(0, date.strftime("%d-%m-%Y"))


# TODO Пофиксить "У вас запись 04-09-2022  на Занято Телефон клиента: +375296347998"
# Генератов расписания времени
@dp.callback_query_handler(text="send_work_time")
async def send_work_cal_handler(call: types.CallbackQuery):  # (message: Message):
    # Приводим к формату данные
    format_select_date = userSelectData[0]
    format_select_date = format_select_date.split("-")
    format_select_date = (
            format_select_date[0]
            + "."
            + format_select_date[1]
            + "."
            + format_select_date[2]
    )
    # Если нет записи на эту дату то пишем на кнопке занято

    kb_inl_work_clock = types.InlineKeyboardMarkup(resize_keyboard=False, row_width=6)

    if len(db.fetch_from_id_tg_user_select_time(format_select_date)) == 0:
        # Генерация кнопок

        """
        Проверка на пустой список.
        Если список пуст это значит что нет записей на этот день
        Можно выслать обычную клавиатуру
        """

        print("Нет записей на этот день " + str(userSelectData[0]))
        for value in ww1.work_hours_graf_1:
            button_inl_work_clock1 = types.InlineKeyboardButton(
                text=value,
                callback_data=cb_custom.cb_work_time.new(w_time=str(value)),
            )

            kb_inl_work_clock.insert(button_inl_work_clock1)
    else:
        # Генерация кнопок

        """
        Если есть записи на выбраный день,
        то сравниваем выборку из work_time с выборкой из БД.
        Если есть совпадениея меняем текст кнопки на занято
        """

        print("Есть записи на этот день " + str(userSelectData[0]))

        for value in ww1.work_hours_graf_1:

            if value in db.fetch_from_id_tg_user_select_time(format_select_date):

                # print("Занято на " + str(value))
                button_inl_work_clock1 = types.InlineKeyboardButton(
                    text="Занято",
                    callback_data=cb_custom.cb_work_time.new(w_time="Занято"),
                )
                kb_inl_work_clock.insert(button_inl_work_clock1)

            else:

                button_inl_work_clock1 = types.InlineKeyboardButton(
                    text=value,
                    callback_data=cb_custom.cb_work_time.new(w_time=str(value)),
                )
                kb_inl_work_clock.insert(button_inl_work_clock1)

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
    user_select_date = str(userSelectData[0])
    user_select_time = str(userSelectData[1])

    await message.answer(
        text=msg.msg_admin_to_user,
        reply_markup=kb_router.kb_start.kb,
        parse_mode=ParseMode.HTML,
    )

    # Отправка сообщений всем админам бота
    for val in db.fetch_from_admin_profile():
        # Разметка сообщений для админов
        msg_admin = fmt.text(
            fmt.text("🎯🎯🎯У вас запись🎯🎯🎯"),
            fmt.text("на " + user_select_date + " в " + user_select_time),
            fmt.text("🧾🧾🧾Профиль клента🧾🧾🧾"),
            fmt.text("@" + message.from_user.username),
            fmt.text("☎☎☎Телефон клиента☎☎☎"),
            fmt.text(message.contact.phone_number),
            sep="\n",
        )

        await bot.send_message(
            chat_id=val,
            text=msg_admin,
            parse_mode=ParseMode.HTML,
        )

    user_select_date = user_select_date.split("-")
    user_select_time = user_select_time.split("-")

    db.insert_to_users_profile(
        message.contact.user_id,
        message.contact.phone_number,
        message.from_user.username,
        message.contact.first_name,
        message.contact.last_name,
    )
    db.insert_to_tg_bot_users_recording(
        message.contact.user_id,
        message.contact.phone_number,
        message.from_user.username,
        message.contact.first_name,
        message.contact.last_name,
        str(
            user_select_date[0] + "." + user_select_date[1] + "." + user_select_date[2]
        ),
        str(user_select_time[0] + "-" + user_select_time[1]),
        "open",
    )


# Обработка всех текстовых сообщений пользователя
@dp.message_handler(content_types=[types.ContentType.TEXT])
async def msg_text_contact(message: Message):
    await message.reply(
        text=msg.msg_fo_user_text,
        reply_markup=kb_router.kb_inl_cmd_start.kb_inl,
    )
    # print("Набрано человеком " + str(message.text))


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
