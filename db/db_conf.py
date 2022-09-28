import sqlite3

"""
import random


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
    """
    def __init__(
            self,
            id_tg_user_id,
            id_tg_username,
            id_tg_first_name,
            id_tg_last_name,
            id_tg_phone_number,
            # id_tg_msg,
    ):
        self.id_tg_user_id = id_tg_user_id
        # self.id_tg_msg = str(id_tg_msg)
        self.id_tg_username = str(id_tg_username)
        self.id_tg_first_name = str(id_tg_first_name)
        self.id_tg_last_name = str(id_tg_last_name)
        self.id_tg_phone_number = id_tg_phone_number
    
    def __str__(self):
        return str(
            [
                [self.id_tg_user_id],
                # [self.id_tg_msg],
                [self.id_tg_phone_number],
                [self.id_tg_username],
                [self.id_tg_first_name],
                [self.id_tg_last_name],
            ]
        )

   
    def __del__(self):
        # Закрываем соединение с ДБ
        self.db_cur.close()
        self.db_conn.close()
    """

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
                "SELECT "
                "id_tg_user_select_date, id_tg_user_select_time, users_recording_status"
                " FROM tg_bot_users_recording "
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
                "SELECT id_tg_user_select_date, id_tg_user_select_time "
                "FROM tg_bot_users_recording "
                "WHERE users_recording_status='open'"
                "ORDER BY id_tg_user_select_date, id_tg_user_select_time "
            )
            # print(res.fetchall())
            # print("tg_bot_users_recording FETCH ")
            return res.fetchall()
        except Exception:
            print("fetch_from_tg_bot_users_open_recording ERR ")

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

    '''  
    # Создание таблицы для логирования сообщений

    def table_creat_users_msg(self):
            try:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS "tg_bot_users_msg" (
                    "id"	INTEGER,
                    "id_tg"	INTEGER,
                    "id_tg_msg"	TEXT,
                    PRIMARY KEY("id" AUTOINCREMENT)
                    );
                    """
                )
                conn.commit()
                return print("tg_bot_users_msg CREAT")
            except Exception:
                return print("tg_bot_users_msg ERR")

        # Логирования сообщений
        def table_insert_to_users_msg(self):
            try:
                add_to = (self.id_tg, self.id_tg_msg)
                cur.execute("INSERT INTO tg_bot_users_msg VALUES(null, ?, ?);", add_to)
                conn.commit()
                return print("tg_bot_users_msg ADD " + str(add_to))
            except Exception:
                return print("tg_bot_users_msg ERR " + str(add_to))

        def select_id_tg_ms_for_ig_msg(self, id_tg):
            cur.execute("SELECT * FROM tg_bot_users_msg WHERE id_tg =" + str(id_tg))
            conn.commit()
            rows = cur.fetchall()
            return list(rows)
'''


'''
db_class = ClassForDB()
# print(db_class)
# print(db_class.select_id_tg_ms_for_ig_msg("8628"))


db_class.table_creat_users_profile()
for counter in range(0, 10):
    db_class.table_insert_to_users_profile()

db_class.table_creat_admin_profile()
for counter in range(0, 10):
    db_class.table_insert_to_admin_profile()
"""
db_class.table_creat_users_msg()
for counter in range(0, 10):
    db_class.table_insert_to_users_msg()
"""
'''
