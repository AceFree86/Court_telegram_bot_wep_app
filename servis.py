import json
from datetime import datetime

from aiogram import Bot, types

import keyboards as keyboard
import string_container as str_container
from config import TOKEN
from data_base import Database

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

database = Database()


async def show_list(message):
    result = "Статистика користувачів:\n\n" + "\n".join(f"{row[0]}: {row[2]}" for row in database.user_list())
    await bot.send_message(message.chat.id, result, reply_markup=keyboard.create_main_markup())


async def format_date(date_string):
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

        with open(pad_file['pad'], 'r', encoding='utf-8') as f:
            file_content = f.read()
            data = json.loads(file_content)

            format_str = await format_date(str_data['dob'])
            filtered_data = [i for i in data if format_str in i['date']
                             or format_str.lower().replace('"', " ").replace("'", " ") in i['involved']
                             .lower().replace('"', " ").replace("'", " ")
                             or format_str in i['number']
                             and str_data['formset'] in i['forma']
                             and str_data['court'] in i['judge']]

            if not filtered_data:
                option = str_container.callback_btn[index]
                await bot.send_message(web_app_message.chat.id,
                                       "Якщо нічого не з'явилося, можливо справа ще не призначена до розгляду або Ви"
                                       " вибрали вихідний день. Ви також можете відвідати вебпортал.",
                                       reply_markup=keyboard.btn_callback_markup(option["url"], "callback_date"))
                return

            for i in filtered_data:
                news = (f"Суддя : {i['judge']}\n"
                        f"Номер справи : {i['number']}\n"
                        f"Дата/Час : <b>{i['date']}</b> год.\n"
                        f"Сторони по справі:\n<b>{i['involved']}</b>\n"
                        f"Суть : <b>{i['description']}</b>")
                await bot.send_message(web_app_message.chat.id, news, reply_markup=keyboard.btn_court_list_markup())
