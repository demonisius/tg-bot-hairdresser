import sqlite3
import random

simIdTg = random.randint(1000, 9999)
simPhone = random.randint(10000, 99999)
simMsg = "Msg: simMsg " + str(random.randint(10000, 99999))
simName = "Name: simName " + str(random.randint(10000, 99999))
simNick = "Nick: simNick " + str(random.randint(10000, 99999))

conn = sqlite3.connect("db/test_database.db")
cur = conn.cursor()


class CLASSDB:

    """
    Класс для работы с ДБ
    Профили пользователей
    Логирование сообщений
    Список админиситраторов бота
    """

    def __init__(self, id_tg, id_tg_msg, id_tg_phone_num, id_tg_nick, id_tg_name):
        self.id_tg = id_tg
        self.id_tg_msg = str(id_tg_msg)
        self.id_tg_phone_num = id_tg_phone_num
        self.id_tg_nick = str(id_tg_nick)
        self.id_tg_name = str(id_tg_name)

    def __str__(self):
        return str(
            [
                [self.id_tg],
                [self.id_tg_msg],
                [self.id_tg_phone_num],
                [self.id_tg_nick],
                [self.id_tg_name],
            ]
        )

    # Создание таблицы для профилей пользователей
    def table_creat_users_profile(self):
        try:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS "tg_bot_users_profile" (
                "id"	INTEGER,
                "id_tg"	INTEGER,
                "id_tg_phone_num"	INTEGER,
                "id_tg_nick" TEXT,
                "id_tg_name" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                """
            )
            conn.commit()
            return print("tg_bot_users_profile CREAT")
        except Exception:
            return print("tg_bot_users_profile ERR")

    # Добаление нового профиля пользователя
    def table_insert_to_users_profile(self):
        try:
            add_to = (
                self.id_tg,
                self.id_tg_phone_num,
                self.id_tg_nick,
                self.id_tg_name,
            )
            cur.execute(
                "INSERT INTO tg_bot_users_profile VALUES(null, ?, ?, ?, ?);", add_to
            )
            conn.commit()
            return print("tg_bot_users_profile ADD " + str(add_to))
        except Exception:
            return print("tg_bot_users_profile ERR " + str(add_to))

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

    # Создание таблицы админиситраторов бота

    def table_creat_admin_profile(self):
        try:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS "tg_bot_admin_profile" (
                "id"	INTEGER,
                "id_tg"	INTEGER,
                "id_tg_phone_num"	INTEGER,
                "id_tg_nick" TEXT,
                "id_tg_name" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                """
            )
            conn.commit()
            return print("tg_bot_users_profile CREAT")
        except Exception:
            return print("tg_bot_users_profile ERR")

    # Добаление админиситраторов бота
    def table_insert_to_admin_profile(self):
        try:
            add_to = (
                self.id_tg,
                self.id_tg_phone_num,
                self.id_tg_nick,
                self.id_tg_name,
            )
            cur.execute(
                "INSERT INTO tg_bot_admin_profile VALUES(null, ?, ?, ?, ?);", add_to
            )
            conn.commit()
            return print("tg_bot_admin_profile ADD " + str(add_to))
        except Exception:
            print("tg_bot_admin_profile ERR " + str(add_to))


db_class = CLASSDB(
    id_tg=simIdTg,
    id_tg_msg=simMsg,
    id_tg_phone_num=simPhone,
    id_tg_nick=simNick,
    id_tg_name=simName,
)

print(db_class)


"""
db_class.table_creat_users_profile()
for counter in range(0, 100):
    db_class.table_insert_to_users_profile()

db_class.table_creat_users_msg()
for counter in range(0, 100):
    db_class.table_insert_to_users_msg()

db_class.table_creat_admin_profile()
for counter in range(0, 100):
    db_class.table_insert_to_admin_profile()
"""
