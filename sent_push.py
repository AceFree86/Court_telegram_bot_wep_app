import time
from config import TOKEN, MASTER
from telegram.ext import Updater
from telegram import ParseMode
from data_base import Database
import string_container as str_container
import json

token = TOKEN
admin_id = MASTER

updater = Updater(token)

database = Database()


def send_msg(chat_id, message):
    updater.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
    time.sleep(20)


def get_meetings():
    for row in database.sql_get_meetings(1):
        send_msg(row[1], f"Було знайдено :\n\n{row[2]}")
        database.sql_update_meetings(row[1], row[2], 2)


def start_search():
    for file in str_container.json_files:
        with open(file['pad'], 'r', encoding='utf-8') as f:
            data = json.load(f)
            for row in database.sql_get_user_input(1):
                search_term = row[2].lower().replace('"', " ").replace("'", " ")
                filtered_data = [i for i in data if search_term in
                                 i['involved'].lower().replace('"', " ").replace("'", " ")
                                 or search_term in i['number']]
                for i in filtered_data:
                    msg = (f"Дата/Час : <b>{i['date']}</b> год.\n"
                           f"Номер справи : {i['number']}\n"
                           f"Суддя : {i['judge']}\n"
                           f"__________\n"
                           f"Сторони по справі : <b>{i['involved']}</b>.\n"
                           f"Суть : <b>{i['description']}</b>."
                           f"\n__________")
                    if not database.sql_exists_meetings(row[1], msg):
                        database.sql_insert_meetings(row[1], msg, 1)
                    else:
                        print("yes")


def main():
    try:
        start_search()
        get_meetings()
    except Exception as ex:
        msg = f"Неможливо {ex} відправити повідомлення"
        send_msg(admin_id, msg)


main()
