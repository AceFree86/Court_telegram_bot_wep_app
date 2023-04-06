import json
import sqlite3
from datetime import datetime

from aiogram import Bot, types

import keyboards as nav
from config import TOKEN
from lemmatize_text import UkrainianStemmer
import string_container as str_container

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)


def sql_start():
    global conn, cur
    conn = sqlite3.connect("subscriber.db")
    cur = conn.cursor()
    if conn:
        print("Data base connected OK!")
    conn.commit()


async def sql_add_search_value(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO list_user_input VALUES (?, ?, ?)", tuple(data.values()))
        conn.commit()


async def aql_read(message):
    rows = cur.execute("SELECT * FROM list_user").fetchall()
    result = "Статистика користувачів:\n\n" + "\n".join(f"{row[0]}: {row[2]}" for row in rows)
    await bot.send_message(message.chat.id, result, reply_markup=nav.create_main_markup())


async def read_json_data(message, forma, judges, file_path, state, index):
    text = message.text
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        data = json.loads(file_content)

        stem_obj = UkrainianStemmer(text.replace("'", " "))
        filtered_data = [i for i in data if stem_obj.stem_word() in
                         i["involved"].lower().replace('"', " ").replace("'", " ") or text in i["number"] or
                         text in i["date"] and forma in i["forma"] and judges in i["judge"]]

        if not filtered_data:
            option = str_container.callback_btn[index]
            await bot.send_message(message.chat.id,
                                   "Якщо нічого не з'явилося, можливо неправильно введений номер справи або справа "
                                   "ще не призначена до розгляду.\nВи також можете відвідати вебпортал.",
                                   reply_markup=nav.create_empty_callback_markup(option["url"], option["callback"]))
            await state.finish()
            return

        for i in filtered_data:
            news = (f"Суддя : {i['judge']}\n"
                    f"Номер справи : {i['number']}\n"
                    f"Дата/Час : <b>{i['date']}</b> год.\n"
                    f"Сторони по справі:\n<b>{i['involved']}</b>\n"
                    f"Суть : <b>{i['description']}</b>")
            option = str_container.search_btn[index]
            await bot.send_message(message.chat.id, news,
                                   reply_markup=nav.create_search_markup(
                                       option["name"], option["name2"], option["url"]))
            await state.finish()


async def forma_date(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return date_string
    return date_obj.strftime('%d.%m.%Y')


async def read_wep_app(web_app_message):
    json_data = web_app_message.web_app_data
    json_str = json_data.data
    index = str_container.button_mapping.get(json_data.button_text)

    if json_str is not None and index is not None:
        pad_file = str_container.json_files[index]
        str_data = json.loads(json_str)
        print(str_data)
        with open(pad_file["pad"], "r", encoding="utf-8") as f:
            file_content = f.read()
            data = json.loads(file_content)

            f_str = await forma_date(str_data['dob'])
            filtered_data = [i for i in data if f_str in i["date"]
                             or f_str.lower().replace('"', " ").replace("'", " ") in i["involved"]
                             .lower().replace('"', " ").replace("'", " ")
                             or f_str in i["number"]
                             and str_data['formset'] in i["forma"]
                             and str_data['court'] in i["judge"]]

            if not filtered_data:
                option = str_container.callback_btn[index]
                await bot.send_message(web_app_message.chat.id,
                                       "Якщо нічого не з'явилося, можливо справа ще не призначена до розгляду або Ви"
                                       " вибрали вихідний день.\nВи також можете відвідати вебпортал.",
                                       reply_markup=nav.create_empty_callback_markup(option["url"], option["callback"]))
                return

            for i in filtered_data:
                news = (f"Суддя : {i['judge']}\n"
                        f"Номер справи : {i['number']}\n"
                        f"Дата/Час : <b>{i['date']}</b> год.\n"
                        f"Сторони по справі:\n<b>{i['involved']}</b>\n"
                        f"Суть : <b>{i['description']}</b>")
                option = str_container.search_btn[index]
                await bot.send_message(web_app_message.chat.id, news, reply_markup=nav.create_search_markup(
                    option["name"], option["name2"], option["url"]))
