import sqlite3
import random

"""
simIdTg = 503415978  # random.randint(1000, 9999)  # 503415978
simPhone = +375296347998  # random.randint(10000, 99999)  # +375296347998
simMsg = "Msg: simMsg " + str(random.randint(10000, 99999))
simNick = "Nick: simNick " + str(random.randint(10000, 99999))
simFirst_name = "Nick: simFirst_name " + "Sergg"
simLast_name = "Nick: simLast_name " + "Tech"
simUsername = "Name: simUsername " + "SerggTech"
simUsers_recording_status = ['open','close']
"""


class ClassForDB:
    """
    TODO Вынести запросы к дб в отдельный файл
    Класс для работы с ДБ
    Профили пользователей
    Логирование сообщений
    Список админиситраторов бота

    message.contact.user_id,
    message.from_user.username,
    message.contact.phone_number,
    message.contact.first_name,
    message.contact.last_name,
    503415978 SerggTech +375296347998 Sergg Tech
    """

    db_conn = sqlite3.connect("db/database.db")
    db_cur = db_conn.cursor()

    # Создание таблицы для профилей пользователей
    def creat_users_profile(self):
        try:
            self.db_cur.execute(
                """
                CREATE TABLE IF NOT EXISTS "tg_bot_users_profile" (
                "id"	INTEGER,
                "id_tg_user_id"	INTEGER,
                "id_tg_phone_number"	INTEGER,
                "id_tg_username" TEXT,
                "id_tg_first_name" TEXT,
                "id_tg_last_name" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                """
            )
            self.db_conn.commit()
            # return print("tg_bot_users_profile CREAT")
        except Exception:
            return print("tg_bot_users_profile ERR")

    # Добаление нового профиля пользователя
    def insert_to_users_profile(
        self,
        id_tg_user_id,
        id_tg_phone_number,
        id_tg_username,
        id_tg_first_name,
        id_tg_last_name,
    ):
        try:
            add_to = (
                id_tg_user_id,
                id_tg_phone_number,
                id_tg_username,
                id_tg_first_name,
                id_tg_last_name,
            )
            self.db_cur.execute(
                "INSERT INTO tg_bot_users_profile VALUES(null, ?, ?, ?, ?, ?);", add_to
            )
            self.db_conn.commit()
            # return print("tg_bot_users_profile ADD " + str(add_to))
        except Exception:
            return print("tg_bot_users_profile ERR " + str(add_to))

    # Создание таблицы админиситраторов бота

    def creat_admin_profile(self):
        try:
            self.db_cur.execute(
                """
                CREATE TABLE IF NOT EXISTS "tg_bot_admin_profile" (
                "id"	INTEGER,
                "id_tg_user_id"	INTEGER,
                "id_tg_phone_number"	INTEGER,
                "id_tg_username" TEXT,
                "id_tg_first_name" TEXT,
                "id_tg_last_name" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                """
            )
            self.db_conn.commit()
            # return print("tg_bot_admin_profile CREAT")
        except Exception:
            return print("tg_bot_admin_profile ERR")

    # Добаление админиситраторов бота
    def insert_to_admin_profile(
        self,
        id_tg_user_id,
        id_tg_phone_number,
        id_tg_username,
        id_tg_first_name,
        id_tg_last_name,
    ):
        try:
            add_to = (
                id_tg_user_id,
                id_tg_phone_number,
                id_tg_username,
                id_tg_first_name,
                id_tg_last_name,
            )
            self.db_cur.execute(
                "INSERT INTO tg_bot_admin_profile VALUES(null, ?, ?, ?, ?, ?);", add_to
            )
            self.db_conn.commit()
            # return print("tg_bot_admin_profile ADD " + str(add_to))
        except Exception:
            print("tg_bot_admin_profile ERR " + str(add_to))

    # Выборка ИД ТГ Админов
    def fetch_from_admin_profile(self):
        sql = "SELECT id_tg_user_id " "FROM tg_bot_admin_profile "
        try:
            res = self.db_cur.execute(sql)

            format_fetch = []
            for val in res.fetchall():
                format_fetch.append(val[0])

            return format_fetch
        except Exception:
            print("fetch_from_admin_profile ERR ")

    # Создание таблицы записей на прием
    def creat_tg_bot_users_recording(self):
        try:
            self.db_cur.execute(
                """
                CREATE TABLE IF NOT EXISTS "tg_bot_users_recording" (
                "id"    INTEGER,
                "id_tg_user_id"    INTEGER,
                "id_tg_phone_number"    INTEGER,
                "id_tg_first_name"    TEXT,
                "id_tg_last_name"    TEXT,
                "id_tg_username"    TEXT,
                "id_tg_user_select_date"    BLOB,
                "id_tg_user_select_time"    BLOB,
                "users_recording_status"  TEXT,
                PRIMARY    KEY("id"    AUTOINCREMENT)
                );
                """
            )
            self.db_conn.commit()
            # return print("tg_bot_users_recording CREAT")
        except Exception:
            return print("creat_tg_bot_users_recording ERR")

    # Добаление записей на прием
    def insert_to_tg_bot_users_recording(
        self,
        id_tg_user_id,
        id_tg_phone_number,
        id_tg_username,
        id_tg_first_name,
        id_tg_last_name,
        id_tg_user_select_date,
        id_tg_user_select_time,
        users_recording_status,
    ):

        try:
            add_to = (
                id_tg_user_id,
                id_tg_phone_number,
                id_tg_username,
                id_tg_first_name,
                id_tg_last_name,
                id_tg_user_select_date,
                id_tg_user_select_time,
                users_recording_status,
            )
            self.db_cur.execute(
                "INSERT INTO tg_bot_users_recording VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?);",
                add_to,
            )
            self.db_conn.commit()
            # return print("tg_bot_users_recording ADD " + str(add_to))
        except Exception:
            print("insert_to_tg_bot_users_recording ERR " + str(add_to))

    # Выборка всех записей на прием
    def fetch_from_tg_bot_users_all_recording(self):
        try:
            res = self.db_cur.execute(
                "SELECT id_tg_user_select_date, id_tg_user_select_time, users_recording_status "
                "FROM tg_bot_users_recording "
                "ORDER BY id_tg_user_select_date"
            )
            # print(res.fetchall())
            # print("tg_bot_users_recording FETCH ")
            return res.fetchall()
        except Exception:
            print("fetch_from_tg_bot_users_all_recording ERR ")

    # Выборка открытых записей на прием
    def fetch_from_tg_bot_users_open_recording(self):
        try:
            res = self.db_cur.execute(
                "SELECT id_tg_user_select_date, id_tg_user_select_time ,id "
                "FROM tg_bot_users_recording "
                "WHERE users_recording_status='open' "
                "ORDER BY id_tg_user_select_date, id_tg_user_select_time "
            )
            # print(res.fetchall())
            # print("tg_bot_users_recording FETCH ")
            return res.fetchall()
        except Exception:
            print("fetch_from_tg_bot_users_open_recording ERR ")

    def update_from_tg_bot_users_open_recording(self, recording_id):
        try:
            sql = (
                "UPDATE tg_bot_users_recording"
                " SET users_recording_status = 'close' "
                " WHERE id = '" + recording_id + "'"
            )
            self.db_cur.execute(sql)
            self.db_conn.commit()
            pass
        except Exception:
            print("update_from_tg_bot_users_open_recording ERR ")

    # Выборка закрытых записей на прием
    def fetch_from_tg_bot_users_close_recording(self):
        try:
            res = self.db_cur.execute(
                "SELECT id_tg_user_select_date, id_tg_user_select_time "
                "FROM tg_bot_users_recording "
                "WHERE users_recording_status='close'"
                "ORDER BY id_tg_user_select_date, id_tg_user_select_time "
            )
            # print(res.fetchall())
            return res.fetchall()
        except Exception:
            print("fetch_from_tg_bot_users_close_recording ERR ")

    # Выборка для определения занятых часов на определённую дату приема
    def fetch_from_id_tg_user_select_time(self, select_date):
        # print('def '+select_date)
        sql = (
            "SELECT id_tg_user_select_time "
            "FROM tg_bot_users_recording "
            "WHERE id_tg_user_select_date = '" + select_date + "' "
            "ORDER BY id_tg_user_select_date, id_tg_user_select_time "
        )

        try:
            res = self.db_cur.execute(sql)

            # Приводим к формату данные# Приводим к формату данные
            format_fetch = []
            for val in res.fetchall():
                format_fetch.append(val[0])

            return format_fetch

        except Exception:
            print(Exception.message, Exception.args)
            print("fetch_from_id_tg_user_select_time ERR ")
