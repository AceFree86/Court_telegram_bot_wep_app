from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.types.web_app_info import WebAppInfo

btnMain = KeyboardButton("🔙Назат в меню")


def create_main_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton("📅Дата засідання"), KeyboardButton("📩Сповіщення"))
            .add(KeyboardButton("⚖️Інші суди"), KeyboardButton("☎️Контактні данні"))
            .add(KeyboardButton("📃Електронний Суд"), KeyboardButton("📢Оголошення про виклик")))


def create_empty_url_markup(name, url):
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text=name, url=url)))


def create_empty_callback_markup(url, callback):
    return (InlineKeyboardMarkup(row_width=1)
            .add(InlineKeyboardButton(text="Розклад засідань", url=url, ),
                 InlineKeyboardButton("🔙Назат", callback_data=callback)))


def create_download_app_markup():
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text="Загрузити з Гугл Плей",
                                         url="https://play.google.com/store/apps/details?id=com.floor12apps.ecourt&gl"
                                             "=UA"))
            .insert(InlineKeyboardButton(text="Загрузити з Апп Стор",
                                         url="https://apps.apple.com/ua/app/%D1%94%D1%81%D1%83%D0%B4/id1578245779?l"
                                             "=uk")))


def create_app_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("📲Завантажити офіційний мобільний додаток єСуд")).add(btnMain))


def create_search_markup(name, name2, url):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(name))
            .row(KeyboardButton(name2, web_app=WebAppInfo(url=url)))
            .add(btnMain))


def create_court_list_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton("🗓️Перечинський районний суд"))
            .row(KeyboardButton("🗓️Закарпатський апеляційний суд"))
            .row(KeyboardButton("🗓️Ужгородський міськрайонний суд"))
            .row(KeyboardButton("🗓️Великоберезнянський районний суд"))
            .add(btnMain))


def create_markup(name):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(KeyboardButton(name))
            .add(btnMain))


def create_back_markup(name):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(KeyboardButton(name)))


def create_btn_main_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(btnMain))
