from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.types.web_app_info import WebAppInfo

from string_container import wep_url

btnMain = KeyboardButton(text='🔙Назат в меню')


def create_main_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(text='📅Дата засідання'), KeyboardButton(text='📩Сповіщення'))
            .add(KeyboardButton(text='📃Електронний Суд'), KeyboardButton(text='☎️Контактні данні'))
            .add(KeyboardButton(text="✍🏻Зв'язатися з адміном"), KeyboardButton(text='📢Оголошення про виклик')))

def create_court_list_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(text='📅Перечинський р-н суд', web_app=WebAppInfo(url=wep_url[0]['url'])),
                 KeyboardButton(text='📅Апеляційний суд', web_app=WebAppInfo(url=wep_url[1]['url'])))
            .row(KeyboardButton(text='📅Ужгородський м-р суд', web_app=WebAppInfo(url=wep_url[2]['url'])),
                 KeyboardButton(text='📅В.Березнянський\nр-н суд', web_app=WebAppInfo(url=wep_url[3]['url'])))
            .add(btnMain))


def create_empty_url_markup(name, url):
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text=name, url=url)))


def create_inline_markup():
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text='Зареєструватися',
                                         web_app=WebAppInfo(url='https://starlit-marzipan-56ef4f.netlify.app/register'))))

def create_empty_callback_markup(url, callback):
    return (InlineKeyboardMarkup(row_width=1)
            .add(InlineKeyboardButton(text='Розклад засідань', url=url, ),
                 InlineKeyboardButton(text="🔙Назат", callback_data=callback)))


def create_download_app_markup():
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text='Загрузити з Гугл Плей',
                                         url='https://play.google.com/store/apps/details?id=com.floor12apps.ecourt&gl'
                                             '=UA'))
            .insert(InlineKeyboardButton(text='Загрузити з Апп Стор',
                                         url='https://apps.apple.com/ua/app/%D1%94%D1%81%D1%83%D0%B4/id1578245779?l'
                                             '=uk')))


def create_app_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton(text='📲Завантажити офіційний мобільний додаток єСуд')).add(btnMain))


def create_search_markup(name, name2, url):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(name))
            .row(KeyboardButton(name2, web_app=WebAppInfo(url=url)))
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
