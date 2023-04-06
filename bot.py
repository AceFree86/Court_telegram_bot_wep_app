import asyncio
import logging

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

import keyboards as keyboard
import servis
import string_container as str_container
from config import TOKEN
from data_base import Database

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    servis.sql_start()


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

db = Database("subscriber.db")


class GetCase(StatesGroup):
    case_pr = State()
    case_uz = State()
    case_appel = State()
    case_vb = State()


class RegUser(StatesGroup):
    user_id = State()
    name = State()


@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.first_name)
        await message.answer("👋Доброго дня {0.first_name}!".format(message.from_user))
        await asyncio.sleep(1)
        with open("foto/PRC.jpg", "rb") as foto:
            await message.answer_photo(foto, str_container.opus_bot)
            await asyncio.sleep(3)
            await message.answer("{0}".format(str_container.instruction), reply_markup=keyboard.create_main_markup())


@dp.message_handler(commands=['list'])
async def check(message: types.Message):
    await servis.aql_read(message)


@dp.message_handler(Command('pr') | Text(equals=['📅Дата засідання']))
@dp.message_handler(Command('appel') | Text(equals=['⚖️Закарпатський апеляційний суд']))
@dp.message_handler(Command('uz') | Text(equals=['⚖️Ужгородський міськрайонний суд']))
@dp.message_handler(Command('vb') | Text(equals=['⚖️Великоберезнянський районний суд']))
async def commands_handler(message: types.Message):
    text = message.text
    option_index = None
    if text in ['📅Дата засідання', '/pr']:
        option_index = 0
    elif text in ['⚖️Закарпатський апеляційний суд', '/appel']:
        option_index = 1
    elif text in ['⚖️Ужгородський міськрайонний суд', '/uz']:
        option_index = 2
    elif text in ['⚖️Великоберезнянський районний суд', '/vb']:
        option_index = 3

    if option_index is not None:
        option = str_container.search_btn[option_index]
        await message.answer(f"{message.from_user.first_name} {str_container.meeting_date}",
                             reply_markup=keyboard.create_search_markup(option["name"], option["name2"], option["url"]))


@dp.message_handler(content_types='web_app_data')
async def data(web_app_message):
    await servis.read_wep_app(web_app_message)


@dp.message_handler()
async def bot_message(message: types.Message):
    text = message.text

    if text == "🔙Назат в меню":
        await message.answer("Головне меню", reply_markup=keyboard.create_main_markup())

    elif text == "☎️Контактні данні":
        name = "🗺Карти проїзду"
        await message.answer("<u><b>{0.first_name} {1}".format(message.from_user, str_container.contact),
                             reply_markup=keyboard.create_markup(name))

    elif text == "🗺Карти проїзду":
        await message.answer("Карти проїзду 🚗. Натисніть на кнопку, щоб переміститися на бажану карту",
                             reply_markup=keyboard.create_btn_main_markup())

        with open("foto/perechin.jpg", "rb") as foto:
            name = "Переміститися на Apple Карту"
            url = "https://maps.apple.com/place?address=48.735389,22.476694&q"
            await message.answer_photo(foto, reply_markup=keyboard.create_empty_url_markup(name, url))

        with open("foto/perechin1.jpg", "rb") as foto:
            name = "Переміститися на Google Карту"
            url = "https://goo.gl/maps/sNThx2MEs5VCuy2z9"
            await message.answer_photo(foto, reply_markup=keyboard.create_empty_url_markup(name, url))

    elif text == "📢Оголошення про виклик":
        name = "Переміститися в Оголошення"
        url = "https://pr.zk.court.gov.ua/sud0708/gromadyanam//"
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.notice),
                             reply_markup=keyboard.create_empty_url_markup(name, url))

    elif text == "📃Електронний Суд":
        with open("foto/electroniccourt.jpg", "rb") as foto:
            await message.answer_photo(foto,
                                       "{0.first_name} {1}".format(message.from_user, str_container.electronic_court),
                                       reply_markup=keyboard.create_app_markup())

    elif text == "📲Завантажити офіційний мобільний додаток єСуд":
        await message.answer("{0}".format(str_container.court_app), reply_markup=keyboard.create_download_app_markup())

    elif text == "⚖️Інші суди":
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.list_court),
                             reply_markup=keyboard.create_court_list_markup())

    elif text == "🎫Пошук за П.І.П. або номером справи":
        name = "🔙_Назат_"
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.input_instruction),
                             reply_markup=keyboard.create_back_markup(name))
        await GetCase.case_pr.set()

    elif text == "🎫Пошук за П.І.П. або номером справи.":
        name = "🔙_Назат_"
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.input_instruction),
                             reply_markup=keyboard.create_back_markup(name))
        await GetCase.case_appel.set()

    elif text == "🎫Пошук за П.І.П. або номером справи..":
        name = "🔙_Назат_"
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.input_instruction),
                             reply_markup=keyboard.create_back_markup(name))
        await GetCase.case_uz.set()

    elif text == "🎫Пошук за П.І.П. або номером справи...":
        name = "🔙_Назат_"
        await message.answer("{0.first_name} {1}".format(message.from_user, str_container.input_instruction),
                             reply_markup=keyboard.create_back_markup(name))
        await GetCase.case_vb.set()

    elif text == "📩Сповіщення":
        name = "/відмова"
        await message.answer("{0.first_name} в цьому розділі можна скористатися сервісом *<b>"
                             "Сповіщення</b>*.\nСуть сервісу проста, Ви отримаєте📩 сповіщення про дату, час "
                             "судового засідання.\n\nЩоб підписатися✍🏻 на сервіс Вам потрібно набрати⌨ "
                             "*<b>так</b>* і відправити📥 та слідувати👉 подальшим інструкціям."
                             "\n\nЩоб скасувати підписку натисніть\nна👉 /cancel.".format(message.from_user),
                             reply_markup=keyboard.create_markup(name))
        await RegUser.user_id.set()


@dp.message_handler(state="*", commands=['cancel'])
@dp.message_handler(Text(equals=['🔙_Назат_'], ignore_case=True), state="*")
async def pass_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    index = str_container.state_mapping.get(current_state)
    await state.finish()
    if index is not None:
        option = str_container.search_btn[index]
        await message.answer("OK!👌 все скасовано.",
                             reply_markup=keyboard.create_search_markup(option["name"], option["name2"], option["url"]))


@dp.message_handler(state=[GetCase.case_pr, GetCase.case_appel,
                           GetCase.case_uz, GetCase.case_vb], content_types=types.ContentTypes.TEXT)
async def case_handler(message: types.Message, state: FSMContext):
    form = ""
    judges = ""
    current_state = await state.get_state()
    index = list(str_container.case_files.keys()).index(current_state)
    await servis.read_json_data(message, form, judges, str_container.case_files[current_state], state, index)


# реєстрація на message push
@dp.message_handler(state=RegUser.user_id, content_types=types.ContentTypes.TEXT)
async def regUser_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["user_id"] = message.from_user.id
        name = "/відмова"
        await message.answer("{0.first_name} наберіть⌨ прізвище та ім'я або номер справи і відправте📥."
                             "\n\n<b>Попередження</b>❗ \nПрізвище та ім'я набирати можна з малої букви, а"
                             " апостроф в тексті "
                             "заміняється на пробіл.\n\nЩодо номера справи набираємо⌨ відповідно до зразків "
                             "304/555/20 або 555/20.\nІнформацію вказуйте правильно💯."
                             "\n\nПісля сповіщення <b>підписка видалиться</b>🗑."
                             "\n\nЩоб скасувати підписку натисніть \nна👉 /cancel.".format(message.from_user),
                             reply_markup=keyboard.create_markup(name))
        await RegUser.name.set()


@dp.message_handler(state=RegUser.name, content_types=types.ContentTypes.TEXT)
async def regUser2_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await servis.sql_add_search_value(state)
    await state.finish()
    await message.answer(
        "{0.first_name} Ви підписалися👍, очікуйте на сповіщення.".format(message.from_user),
        reply_markup=keyboard.create_main_markup())


@dp.callback_query_handler(text_startswith="callback_")
async def callback_btn(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    index = str_container.callback_mapping.get(callback_query.data)
    if index is not None:
        option = str_container.search_btn[index]
        await callback_query.message.answer(
            "{0.first_name} {1}".format(callback_query.message.from_user, str_container.meeting_date),
            reply_markup=keyboard.create_search_markup(option["name"], option["name2"], option["url"]))
        await callback_query.answer("Розділ 📅Дата засідання")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except Exception as e:
        print(f"An error occurred while running the program: {e}")
