from aiogram import types
from aiogram.types import Message


class WorkWindow:
    # Список с рабочими окнами
    work_hours_graf_1 = [
        " ",
        "8:00",
        "8:30",
        "9:00",
        "9:30",
        "10:00",
        "10:30",
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
        "16:00",
        "16:30",
        "17:00",
        "17:30",
        "18:00",
    ]
    work_hours_graf_2 = [
        "8:00",
        "8:30",
        "9:00",
        "9:30",
        "10:00",
        "10:30",
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
        "16:00",
        "16:30",
    ]

    # def __init__(self, workhours):
    # self.value = None
    # self.workhours = []

    # Генератор кнопок с рабочими часами
    async def work_graf_1_cal_handler(self, message: Message):
        await message.answer("Пожалуйтса выберите время визита: ")

        menu_kb_inl = types.InlineKeyboardMarkup(resize_keyboard=False, row_width=6)
        counter = 0
        for value in self.work_hours_graf_1[0:-1]:
            button_inl_work_clock1 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter],
                callback_data=self.work_hours_graf_1[counter],
            )
            button_inl_work_clock2 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter + 1],
                callback_data=self.work_hours_graf_1[counter + 1],
            )
            button_inl_work_clock3 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter + 2],
                callback_data=self.work_hours_graf_1[counter + 2],
            )
            button_inl_work_clock4 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter + 3],
                callback_data=self.work_hours_graf_1[counter + 3],
            )
            button_inl_work_clock5 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter + 4],
                callback_data=self.work_hours_graf_1[counter + 4],
            )
            button_inl_work_clock6 = types.KeyboardButton(
                text=self.work_hours_graf_1[counter + 5],
                callback_data=self.work_hours_graf_1[counter + 5],
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

        await message.reply("Выберите время: ", reply_markup=menu_kb_inl)

    async def print_work_hours(self):
        for value in self.work_hours_graf_1:
            print(str(value))
        # return self.value


# ww1 = WorkWindow()
# print(ww1.work_hours_graf_1)
# ww1.work_graf_1_cal_handler()
