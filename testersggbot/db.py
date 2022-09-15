import sqlite3

conn = sqlite3.connect("db/database.db")
cur = conn.cursor()

async def add(id_tg, id_tg_msg):
    add_to = (id_tg, id_tg_msg)
    cur.execute("INSERT INTO users VALUES(null, ?, ?);", add_to)
    conn.commit()


async def creat():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
           id INT PRIMARY KEY AUTOINCREMENT,
           id_tg TEXT,
           id_tg_msg TEXT);
        """
    )
    conn.commit()

# class DBCMD:
