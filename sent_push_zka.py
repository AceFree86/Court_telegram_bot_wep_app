import time
from config import TOKEN, MASTER
from telegram.ext import Updater
from telegram import ParseMode
import sqlite3
import json


token = TOKEN
admin_id = MASTER
json_file = "data/data_zka.json"
sqlite_file = "subscriber.db"


conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()
updater = Updater(token)


def send_msg(chat_id, message):
    updater.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


def check(json_data, sql_data):
    result = []
    for client in sql_data:
        for check_data in json_data:
            if (
                check_data["involved"]
                .lower()
                .replace("'", " ")
                .find(client[1].lower().replace('"', " ").replace("'", " "))
                > -0
            ):
                result.append((client, check_data))
    return result


def del_by_name(name):
    cur.execute(f'DELETE FROM list_zka WHERE involved="{name}"')
    conn.commit()


def main():
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    cur.execute("SELECT * FROM list_zka")
    clients = cur.fetchall()
    res = check(json_data, clients)

    for row, i in res:

        msg = (
            f"👋 Доброго дня!\nЗапит <b>{row[1]}</b>, знайдено:"
            f"\nЗакарпатський апеляційний суд\n"
            f"\nДата/Час засідання:\n<b>{i['date']} год.</b>\n\n"
            f"Номер справи: № {i['number']}\nСклад суду:\n{i['judge']}\n\n"
            f"Сторони по справі:\n<b>{i['involved']}</b>\n\n"
            f"Суть позову:\n<b>{i['description']}</b>\n\n"
            f"\n<b>Підписка видаленна</b>🗑."
            f"\n\n📲 Також подивитися дату судового засідання можна на "
            f"\nвебпорталі https://zka.court.gov.ua/sud4806/gromadyanam/csz/."
        )
        try:
            send_msg(row[0], msg)
            time.sleep(20)
        except Exception as ex:
            msg = f"Неможливо {ex} відправити повідомлення:\n{msg}"
            send_msg(admin_id, msg)
        else:
            del_by_name(row[1])

    return res


main()
