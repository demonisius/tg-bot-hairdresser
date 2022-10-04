import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from db import db_conf

db_conf.ClassForDB()

# from lib import lib

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

# webhook settings
WEBHOOK_HOST = f"https://{HEROKU_APP_NAME}.herokuapp.com"
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = os.getenv("PORT", default=8000)
DB_URL = os.getenv("DATABASE_URL")


class WorkWindow:
    # Список с рабочими окнами
    work_hours_graf_1 = [
        " ",
        " ",
        "8-00",
        "8-30",
        "9-00",
        "9-30",
        "10-00",
        "10-30",
        "11-00",
        "11-30",
        "12-00",
        "12-30",
        "13-00",
        "13-30",
        "14-00",
        "14-30",
        "15-00",
        "15-30",
        "16-00",
        "16-30",
        "17-00",
        "17-30",
        "18-00",
        " ",
    ]
    work_hours_graf_2 = [
        "8-00",
        "8-30",
        "9-00",
        "9-30",
        "10-00",
        "10-30",
        "11-00",
        "11-30",
        "12-00",
        "12-30",
        "12-00",
        "12-30",
        "13-00",
        "13-30",
        "14-00",
        "14-30",
        "15-00",
        "15-30",
        "16-00",
        "16-30",
    ]

    async def print_work_hours(self):
        for value in self.work_hours_graf_1:
            print(str(value))
        # return self.value


# ww1 = WorkWindow()
# print(ww1.work_hours_graf_1)
# ww1.work_graf_1_cal_handler()
