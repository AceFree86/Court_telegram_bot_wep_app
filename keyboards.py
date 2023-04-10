from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.types.web_app_info import WebAppInfo
from string_container import wep_url
from data_base import Database

database = Database()

btnMain = KeyboardButton(text='🔙Назат в меню')


def main_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(text='📅Дата засідання'), KeyboardButton(text='📩Сповіщення'))
            .add(KeyboardButton(text='📃Електронний Суд'), KeyboardButton(text='☎️Контактні данні'))
            .add(KeyboardButton(text="✍🏻Зв'язатися з адміном"), KeyboardButton(text='📢Оголошення про виклик')))


def btn_court_list_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .row(KeyboardButton(text='📅Перечинський р-н суд', web_app=WebAppInfo(url=wep_url[0]['url'])),
                 KeyboardButton(text='📅Апеляційний суд', web_app=WebAppInfo(url=wep_url[1]['url'])))
            .row(KeyboardButton(text='📅Ужгородський м-р суд', web_app=WebAppInfo(url=wep_url[2]['url'])),
                 KeyboardButton(text='📅В.Березнянський\nр-н суд', web_app=WebAppInfo(url=wep_url[3]['url'])))
            .add(btnMain))


def btn_url_markup(name, url):
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text=name, url=url)))


def btn_callback_markup(url, callback):
    return (InlineKeyboardMarkup(row_width=1)
            .add(InlineKeyboardButton(text='Розклад засідань', url=url, ),
                 InlineKeyboardButton(text="🔙Назат", callback_data=callback)))


def btn_lis_app_markup():
    return (InlineKeyboardMarkup(row_width=1)
            .insert(InlineKeyboardButton(text='Загрузити з Гугл Плей',
                                         url='https://play.google.com/store/apps/details?id=com.floor12apps.ecourt&gl'
                                             '=UA'))
            .insert(InlineKeyboardButton(text='Загрузити з Апп Стор',
                                         url='https://apps.apple.com/ua/app/%D1%94%D1%81%D1%83%D0%B4/id1578245779?l'
                                             '=uk')))


def btn_app_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton(text='📲Завантажити офіційний мобільний додаток єСуд')).add(btnMain))


def btn_markup(name):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(KeyboardButton(name))
            .add(btnMain))


def btn_push_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(KeyboardButton(text='📋Список Ваших запис'))
            .add(KeyboardButton(text='🔙_Назат_')))


def btn_callback_list(user_id):
    buttons = [InlineKeyboardButton(text=f"💼{row[2]}", callback_data=f"callback_{row[2]}")
               for row in database.user_list_input(user_id)]
    return (InlineKeyboardMarkup(row_width=1)
            .add(*buttons)
            .add(InlineKeyboardButton(text="🗑Видалити все", callback_data='callback_delete'))
            .add(InlineKeyboardButton(text="🔙Назат", callback_data='callback_main')))


def btn_back_markup(name):
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(KeyboardButton(name)))


def btn_main_markup():
    return (ReplyKeyboardMarkup(resize_keyboard=True)
            .add(btnMain))
