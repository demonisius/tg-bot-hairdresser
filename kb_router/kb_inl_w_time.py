from aiogram import types

kb_inl = types.InlineKeyboardMarkup()
kb_inl.add(
    types.InlineKeyboardButton(text="Выбрать время", callback_data="send_work_time")
)
