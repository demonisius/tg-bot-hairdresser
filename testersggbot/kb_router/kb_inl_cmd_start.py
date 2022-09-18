from aiogram import types

kb_inl = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
button_inl_1 = types.InlineKeyboardButton(text="Услуги", callback_data="Услуги")
button_inl_2 = types.InlineKeyboardButton(text="Мастера", callback_data="Мастера")
button_inl_3 = types.InlineKeyboardButton(text="Контакты", callback_data="Контакты")
button_inl_4 = types.InlineKeyboardButton(
    text="Косультация", callback_data="Косультация"
)
button_inl_5 = types.InlineKeyboardButton(text="Записаться", callback_data="Записаться на приём")


kb_inl.add(
    button_inl_1,
    button_inl_2,
    button_inl_3,
    button_inl_4,
)

kb_inl.add(
    button_inl_5
)

kb_w_time = types.InlineKeyboardMarkup()
kb_w_time.add(
    types.InlineKeyboardButton(text="Нажми меня", callback_data="send_work_time")
)
