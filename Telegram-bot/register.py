import sqlite3

# проверяем, есть ли user_id в базе данных
def user_exists(user_id):
        con = sqlite3.connect('../accountant.db')
        cur = con.cursor()
        result = cur.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

# получаем user_id из БД
def get_user_id(user_id):
        con = sqlite3.connect('../accountant.db')
        cur = con.cursor()
        result = cur.execute("SELECT `user_id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

# добавляем пользователя (user_id) в БД
def add_user(user_id):
        con = sqlite3.connect('../accountant.db')
        cur = con.cursor()
        cur.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return con.commit()

# получаем список всех пользователей
def get_all_users():
    con = sqlite3.connect('../accountant.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT * FROM users; """
    )
    res = res.fetchall()
    con.close()
    return res

# добавляем в БД записи о доходах/расходах
def add_income(user_id, operation, value):
    con = sqlite3.connect('../accountant.db')
    cur = con.cursor()
    cur.execute("INSERT INTO `incom_outcom` (`user_id`, `operation`, `value`) VALUES (?, ?, ?)",
               (get_user_id(user_id),
                operation == "+",
                value))
    return con.commit()

# получаем историю о доходах/расходах за день/месяц/год
def get_income(user_id, within="all"):
    con = sqlite3.connect('../accountant.db')
    cur = con.cursor()

    if (within == "day"):
        result = cur.execute(
            "SELECT * FROM `incom_outcom` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `date`",
            (get_user_id(user_id),))
    elif (within == "week"):
        result = cur.execute(
            "SELECT * FROM `incom_outcom` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date`",
            (get_user_id(user_id),))
    elif (within == "month"):
        result = cur.execute(
            "SELECT * FROM `incom_outcom` WHERE `user_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
            (get_user_id(user_id),))
    else:
        result = cur.execute("SELECT * FROM `incom_outcom` WHERE `user_id` = ? ORDER BY `date`",
            (get_user_id(user_id),))

    return result.fetchall()