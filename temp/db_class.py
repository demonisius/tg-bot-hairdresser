import sqlite3

"""
simIdTg = 503415978  # random.randint(1000, 9999)  # 503415978
simPhone = +375296347998  # random.randint(10000, 99999)  # +375296347998
simMsg = "Msg: simMsg " + str(random.randint(10000, 99999))
simName = (
    "Name: simName " + "SerggTech"
)  # str(random.randint(10000, 99999))  # "SerggTech"
simNick = "Nick: simNick " + str(random.randint(10000, 99999))
simFirst_name = "Nick: simFirst_name " + "Sergg"
simLast_name = "Nick: simLast_name " + "Tech"
simUsername = "Name: simUsername " + "SerggTech"
"""
db_conn = sqlite3.connect("../db/database.db")
db_cur = db_conn.cursor()


class CLASSDB:
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

    def __init__(
        self,
        id_tg_user_id,
        # id_tg_msg,
        id_tg_phone_number,
        id_tg_username,
        id_tg_first_name,
        id_tg_last_name,
    ):
        self.id_tg_user_id = id_tg_user_id
        # self.id_tg_msg = str(id_tg_msg)
        self.id_tg_phone_number = id_tg_phone_number
        self.id_tg_username = str(id_tg_username)
        self.id_tg_first_name = str(id_tg_first_name)
        self.id_tg_last_name = str(id_tg_last_name)

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
        db_cur.close()
        db_conn.close()

    # Создание таблицы для профилей пользователей
    def table_creat_users_profile(self):
        try:
            db_cur.execute(
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
            db_conn.commit()
            return print("tg_bot_users_profile CREAT")
        except Exception:
            return print("tg_bot_users_profile ERR")

    # Добаление нового профиля пользователя
    def table_insert_to_users_profile(self):
        try:
            add_to = (
                self.id_tg_user_id,
                self.id_tg_phone_number,
                self.id_tg_username,
                self.id_tg_first_name,
                self.id_tg_last_name,
            )
            db_cur.execute(
                "INSERT INTO tg_bot_users_profile VALUES(null, ?, ?, ?, ?, ?);", add_to
            )
            db_conn.commit()
            return print("tg_bot_users_profile ADD " + str(add_to))
        except Exception:
            return print("tg_bot_users_profile ERR " + str(add_to))

    # Создание таблицы админиситраторов бота

    def table_creat_admin_profile(self):
        try:
            db_cur.execute(
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
            db_conn.commit()
            return print("tg_bot_users_profile CREAT")
        except Exception:
            return print("tg_bot_users_profile ERR")

    # Добаление админиситраторов бота
    def table_insert_to_admin_profile(self):
        try:
            add_to = (
                self.id_tg_user_id,
                self.id_tg_phone_number,
                self.id_tg_username,
                self.id_tg_first_name,
                self.id_tg_last_name,
            )
            db_cur.execute(
                "INSERT INTO tg_bot_admin_profile VALUES(null, ?, ?, ?, ?, ?);", add_to
            )
            db_conn.commit()
            return print("tg_bot_admin_profile ADD " + str(add_to))
        except Exception:
            print("tg_bot_admin_profile ERR " + str(add_to))

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
db_class = CLASSDB(
    id_tg_user_id=simIdTg,
    # id_tg_msg=simMsg,
    id_tg_phone_number=simPhone,
    id_tg_username=simUsername,
    id_tg_first_name=simFirst_name,
    id_tg_last_name=simLast_name,
)

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
