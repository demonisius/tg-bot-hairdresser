# ЭХО
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


# Генератор часов
@dp.message_handler(commands="clock")
async def cmd_clock(message: types.Message):
    # await ww1.print_work_hours()

    await message.reply("clock")
    menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=False, row_width=6)
    counter = 0
    for value in ww1.work_hours_graf_1[0:-1]:
        button_inl_work_clock1 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter],
            callback_data=ww1.work_hours_graf_1[counter],
        )
        button_inl_work_clock2 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter + 1],
            callback_data=ww1.work_hours_graf_1[counter + 1],
        )
        button_inl_work_clock3 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter + 2],
            callback_data=ww1.work_hours_graf_1[counter + 2],
        )
        button_inl_work_clock4 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter + 3],
            callback_data=ww1.work_hours_graf_1[counter + 3],
        )
        button_inl_work_clock5 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter + 4],
            callback_data=ww1.work_hours_graf_1[counter + 4],
        )
        button_inl_work_clock6 = types.KeyboardButton(
            text=ww1.work_hours_graf_1[counter + 5],
            callback_data=ww1.work_hours_graf_1[counter + 5],
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
        print(counter)
        print(value)
        if counter == 24:
            break

    await message.reply("Выберите время", reply_markup=menu_kb_inl)


# Специальные команды
@dp.message_handler(commands="special_buttons")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True),
        types.KeyboardButton(
            text="Создать викторину",
            request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ),
        ),
    )
    await message.answer("Выберите действие:", reply_markup=keyboard)


# Команды Всякое разное
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")
    await db.add(message.from_user.id, message.text)


# Команды Всякое разное
@dp.message_handler(commands="id")
async def cmd_id(message: types.Message):
    await message.reply(message.from_user.id)


# Команда добавления записи  в БД
@dp.message_handler(commands="ad")
async def cmd_ad(message: types.Message):
    await db.add(message.from_user.id, message.text)
    await message.reply("ADD OK")


# Команла добавления таблицы в БД
@dp.message_handler(commands="cr")
async def cmd_cr(message: types.Message):
    await db.creat()
    await message.reply(message.from_user.id)
    await message.reply("Talbe creat")
