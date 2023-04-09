import json
import requests
from telegram.ext import Updater
from telegram import ParseMode
from config import TOKEN, MASTER
from string_container import url_data

token = TOKEN
admin_id = MASTER

updater = Updater(token)


def download_json(url_datas):
    for url_str in url_datas:
        url = url_str['url']
        payload = url_str['payload']
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": url_str['referer']
        }
        response = requests.request(
            "POST", url, headers=headers, data=payload)
        with open(url_str['file_name'], "w", encoding="utf-8") as file_json:
            json.dump(response.json(), file_json, ensure_ascii=False, indent=8)


def send_msg(chat_id, message):
    updater.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


def main():
    try:
        download_json(url_data)
        msg = "Обновився👌, 😎."
        send_msg(admin_id, msg)
    except requests.exceptions.ConnectionError as e:
        msg = f"🤚Не обновився🤬, {e}."
        send_msg(admin_id, msg)


if __name__ == "__main__":
    main()
