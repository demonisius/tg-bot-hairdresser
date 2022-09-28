from db import db_conf

db_conf.ClassForDB
# from lib import lib


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
