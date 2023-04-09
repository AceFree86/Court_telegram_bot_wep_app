import asyncio
import logging

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

import keyboards as keyboard
import servis
import string_container as str_container
from config import TOKEN
from data_base import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

db = Database("subscriber.db")


class GetUserData(StatesGroup):
    input_user = State()


@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.first_name)
        await message.answer(f"👋Доброго дня {message.from_user.first_name}!")
        await asyncio.sleep(1)
        with open("foto/PRC.jpg", "rb") as foto:
            await message.answer_photo(foto, str_container.opus_bot)
            await asyncio.sleep(1)
            await message.answer("{0}".format(str_container.instruction), reply_markup=keyboard.create_main_markup())


@dp.message_handler(commands=['list'])
async def read_sqlite(message: types.Message):
    await servis.show_list(message)


@dp.message_handler(content_types='web_app_data')
async def data(web_app_message):
    await servis.read_wep_app(web_app_message)


@dp.message_handler()
async def bot_message(message: types.Message):
    text = message.text
    if text in ["🔙Назат в меню", "🔙_Назат_"]:
        await message.answer("Головне меню", reply_markup=keyboard.create_main_markup())
    elif text == '☎️Контактні данні':
        name = '🗺Карти проїзду'
        await message.answer(f"{message.from_user.first_name} <u><b>{str_container.contact}",
                             reply_markup=keyboard.btn_markup(name))
    elif text == '🗺Карти проїзду':
        await message.answer("Карти проїзду 🚗. Натисніть на кнопку, щоб переміститися на бажану карту",
                             reply_markup=keyboard.btn_main_markup())
        with open("foto/perechin.jpg", "rb") as foto:
            name = "Переміститися на Apple Карту"
            url = "https://maps.apple.com/place?address=48.735389,22.476694&q"
            await message.answer_photo(foto, reply_markup=keyboard.btn_url_markup(name, url))
        with open("foto/perechin1.jpg", "rb") as foto:
            name = "Переміститися на Google Карту"
            url = "https://goo.gl/maps/sNThx2MEs5VCuy2z9"
            await message.answer_photo(foto, reply_markup=keyboard.btn_url_markup(name, url))
    elif text == '📢Оголошення про виклик':
        name = "Переміститися в Оголошення"
        url = "https://pr.zk.court.gov.ua/sud0708/gromadyanam//"
        await message.answer(f"{message.from_user.first_name} {str_container.notice}",
                             reply_markup=keyboard.btn_url_markup(name, url))
    elif text == '📃Електронний Суд':
        with open("foto/electroniccourt.jpg", "rb") as foto:
            await message.answer_photo(foto, f"{message.from_user.first_name} {str_container.electronic_court}",
                                       reply_markup=keyboard.btn_app_markup())
    elif text == '📲Завантажити офіційний мобільний додаток єСуд':
        await message.answer(f"{str_container.court_app}", reply_markup=keyboard.btn_lis_app_markup())
    elif text == "✍🏻Зв'язатися з адміном":
        await message.answer(f"{message.from_user.first_name} {str_container.list_court}",
                             reply_markup=keyboard.btn_court_list_markup())
    elif text == '📅Дата засідання':
        await message.answer(f"{message.from_user.first_name} {str_container.meeting_date}",
                             reply_markup=keyboard.btn_court_list_markup())
    elif text == '📩Сповіщення':
        await message.answer(f"{message.from_user.first_name} {str_container.push}",
                             reply_markup=keyboard.btn_back_markup('🔙_Назат_'))
        await GetUserData.input_user.set()
    elif text == '📋Список Ваших запис':
        await message.answer(f"{message.from_user.first_name} щоб видалити Ваш запис виберіть зі списку та "
                             f"натисніть на нього. Список записів :",
                             reply_markup=keyboard.btn_back_markup('🔙_Назат_'))
        await GetUserData.input_user.set()



@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals=['🔙_Назат_'], ignore_case=True), state="*")
async def pass_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.answer("OK!👌 все скасовано.", reply_markup=keyboard.create_main_markup())


@dp.message_handler(state=GetUserData.input_user, content_types=types.ContentTypes.TEXT)
async def regUser_handler(message: types.Message, state: FSMContext):
    user_input = {"USER_ID": message.from_user.id, "USER_INPUT": message.text, "STATE": 1}
    await servis.sql_add_search_value(user_input)
    await message.answer(f"{message.from_user.first_name} Ви підписалися👍, очікуйте на сповіщення 😎.", reply_markup=keyboard.create_main_markup())
    await state.finish()


@dp.callback_query_handler(text_startswith="callback_")
async def callback_btn(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    index = str_container.callback_mapping.get(callback_query.data)
    if index is not None:
        await callback_query.message.answer(f"{callback_query.from_user.first_name} {str_container.meeting_date}",
                                            reply_markup=keyboard.btn_court_list_markup())
        await callback_query.answer("Розділ 📅Дата засідання")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"An error occurred while running the program: {e}")
