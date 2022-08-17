# Телеграм-бот учета доходов и расходов
# библиотека - pyTelegramBotAPI
# БД- SQLite3 (SQLiteStudio)

import telebot
import re

from register import add_income, get_income, user_exists, get_all_users, add_user

bot = telebot.TeleBot('5509558474:AAFbJRCrkTji9CKRY5zHL_HbEWIi4G_qpFQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Телеграм-бот Учета доходов и расходов! Нажмите /register для регистрации')


@bot.message_handler(commands=['register'])
def register(message):
    user_id = message.chat.id
    if user_exists(user_id):
        bot.send_message(user_id, 'Вы уже зарегистрированы!')
    else:
        # bot.send_message(message.chat.id, 'Введите, пожалуйста, Ваше имя и фамилию')
        # bot.register_next_step_handler(message, read_name)
        bot.send_message(message.chat.id, f"Спасибо за регистрацию!\n"
                                          f"Для внесения дохода введите /income и сумму через пробел\n"
                                          f"Для внесения расхода введите /outcome и сумму через пробел\n"
                                          f"Для просмотра истории Ваших доходов/расходов введите /history и интересующий Вас период (day, month, year)\n"
                                          f"Для просмотра всех пользователей Телеграм-бота введите /all\n"
                                          f"Для просмотра списка команд введите /help ")
        add_user(message.chat.id)


# def read_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f"Спасибо за регистрацию! ")
#     create_user(message.chat.id, name)

@bot.message_handler(commands=['outcome', 'income'])
def in_out(message):
    cmd_variants = (('/outcome'), ('/income'))
    operation = '-' if message.text.startswith(cmd_variants[0]) else '+'

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    if(len(value)):
        x = re.findall(r"\d+(?:.\d+)?", value)
        if(len(x)):
            value = float(x[0].replace(',', '.'))

            add_income(message.chat.id, operation, value)

            if(operation == '-'):
                return bot.send_message(message.chat.id, f"Запись о расходе успешно добавлена в базу данных!")
            else:
                return bot.send_message(message.chat.id, f"Запись о доходе успешно добавлена в базу данных!")
        else:
            return bot.send_message(message.chat.id, f"Не удалось определить сумму!")
    else:
        return bot.send_message(message.chat.id, f"Не введена сумма!")


@bot.message_handler(commands=['history', 'h'])
def history(message):
    cmd_variants = ('/history', '/h')
    within_als = {
        "day": ('today', 'day', 'сегодня', 'день'),
        "month": ('month', 'месяц'),
        "year": ('year', 'год'),
    }

    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    within = 'day'
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    records = get_income(message.chat.id, within)

    if(len(records)):
        answer = f"История операций за {within_als[within][-1]}:\n\n"

        for r in records:
            answer += ("Расход" if not r[1] else "Доход")
            answer += f" - {r[2]} - "
            answer += f" дата: ({r[3]})\n"

        return bot.send_message(message.chat.id, f"{answer}")
    else:
        return bot.send_message(message.chat.id, f"Записей не обнаружено!")


@bot.message_handler(commands=['all'])
def register(message):
    all_users = get_all_users()
    bot.send_message(message.chat.id, str(all_users))


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, f"Список доступных команд Телеграм-бота Учета расходов и доходов:\n"
                f"Для внесения дохода введите /income и сумму через пробел\n"
                f"Для внесения расхода введите /outcome и сумму через пробел\n"
                f"Для просмотра истории Ваших доходов/расходов введите /history и интересующий Вас период (day, month, year)\n"
                f"Для просмотра всех пользователей Телеграм-бота введите /all\n"
                f"Для просмотра списка команд введите /help ")

bot.infinity_polling()