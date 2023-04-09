opus_bot = """Я Віртуальний асистент <b>Перечинського районного суду</b>.
Я вмію находити дату судового засідання за прізвищем, ім'ям і за номером справи, а також сповіщаю про дату і час засідання."""

instruction = """Наше спілкування буде проходити так:
- Вибираєте🕹 розділ в меню;
- Натискаєте📲 на кнопки в меню;
- А я Вам відпишу📨."""

contact = """ контактні дані:</b></u>

📍E-mail📧: inbox@pr.zk.court.gov.ua

📍Телефон📞: (03145)2-11-96

📍Адреса📮: пл. Народна, 15, м. Перечин, 89200.

📍Щоб знайти Перечинський р-н суд натисніть на кнопку Карти🗺 проїзду 🚖 👇."""

notice = """ перейшовши на вебпортал, можна передивитися всі оголошення про виклик до Перечинського районного суду."""

electronic_court = " електронний суд дозволяє подавати учасникам судового процесу " \
                   "до суду документи в електронному вигляді, а також надсилати таким учасникам " \
                   'процесуальних документів в електронному вигляді, паралельно з документами у ' \
                   'паперовому вигляді відповідно до процесуального ' \
                   'процесуального законодавства.\n\n<a href="https://id.court.gov.ua/">' \
                   "Перейти в Електронний Суд🔗.</a>\n\n."

court_app = "Також Ви можете скористатися Нашим офіційним мобільним додатком <b>Електронного суду в " \
            "Україні єСуд</b> призначеним для доступу до Електронного суду з мобільних пристроїв. " \
            "<b>Для використання додатку Вам необхідно бути зареєстрованим в електронному " \
            'кабінеті</b>.\n\n<a href="https://cabinet.court.gov.ua">Перейти в Електронний' \
            " кабінет🔗.</a>\n\n."

push = " в цьому розділі можна скористатися сервісом *<b>" \
       "Сповіщення</b>*.\nСуть сервісу проста, Ви отримаєте📩 повідомлення про дату і час " \
       "судового засідання.\n\nЩоб підписатися✍🏻 на сервіс Вам потрібно набрати⌨" \
       " прізвище та ім'я, яке цікавит або номер справи і відправити боту📥." \
       "\n\n<b>Попередження</b>❗\nПрізвище та ім'я набирати можна з малої букви, а " \
       "апостроф в тексті заміняється на пробіл. Щодо номера справи" \
       " набираємо⌨ відповідно до зразків '304/555/20'. <b>Інформацію" \
       "вказуйте правильно</b>💯." \
       "\n\nЩоб скасувати підписку натисніть на👉 /cancel або кнопку 🔙_Назат_."

admin = " Ви можете написати зауваження чи прохання адміну." \
        "\n\nЩоб скасувати натисніть на кнопку 🔙_Назат_."

delete_list = 'Щоб видалити Ваш запис виберіть зі списку та натисніть на нього. Список записів: '

map_str = 'Карти проїзду 🚗. Натисніть на кнопку, щоб переміститися на бажану карту'

meeting_date = " в даному розділі можна подивитися дату судового засідання нажавши🕹 на ниже вказані кнопки👇:" \
               "\n\n<b>Ім'я кнопки</b> це суд який доступні для перегляду дати судового засідання." \
               "\n\nКоли Ви натиснете📲 на бажану кнопку з'явиться нове меню пошуку з набором фільтрів пошуку." \
               "\n\n<b>Самі фільтри пошуку</b> гнучкі в налаштуванні." \
               "\n\nЗапуск <b>пошуку</b> починається після натискання на синю кнопку 'Пошук'."

input_instruction = """ набирати можна номер справи або текст з малої букви, апостроф в тексті можна заміняти на пробіл.

<b>Попередження</b>❗, якщо буде введено тільки прізвище або ім’я чи 304 номер, то Вам видасть всі засідання призначені на даний запит.
Щоб скасувати пошук натисніть на👉 /cancel."""

url_data = [
    {"url": "https://pr.zk.court.gov.ua/new.php", "payload": "q_court_id=0708",
     "referer": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/", "file_name": "data/data_pr00.json"},
    {"url": "https://pr.zk.court.gov.ua/new.php", "payload": "q_court_id=0708",
     "referer": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/", "file_name": "data/data_pr.json"},
    {"url": "https://zka.court.gov.ua/new.php", "payload": "q_court_id=4806",
     "referer": "https://zka.court.gov.ua/sud4806/gromadyanam/csz/", "file_name": "data/data_zka.json"},
    {"url": "https://ug.zk.court.gov.ua/new.php", "payload": "q_court_id=0712",
     "referer": "https://ug.zk.court.gov.ua/sud0712/gromadyanam/csz/", "file_name": "data/data_ug.json"},
    {"url": "https://vb.zk.court.gov.ua/new.php", "payload": "q_court_id=0702",
     "referer": "https://vb.zk.court.gov.ua/sud0702/gromadyanam/csz/", "file_name": "data/data_vb.json"}
]

url_btn = [
    {"url": "https://pr.zk.court.gov.ua/sud0708/gromadyanam/csz/"},
    {"url": "https://zka.court.gov.ua/sud4806/gromadyanam/csz/"},
    {"url": "https://ug.zk.court.gov.ua/sud0712/gromadyanam/csz/"},
    {"url": "https://vb.zk.court.gov.ua/sud0702/gromadyanam/csz/"}
]

name_btn = [
    {"name": "Переміститися на Apple Карту", "url": "https://maps.apple.com/place?address=48.735389,22.476694&q"},
    {"name": "Переміститися на Google Карту", "url": "https://goo.gl/maps/sNThx2MEs5VCuy2z9"},
    {"name": "Переміститися в Оголошення", "url": "https://pr.zk.court.gov.ua/sud0708/gromadyanam"}
]

wep_url = [
    {"url": "https://starlit-marzipan-56ef4f.netlify.app"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/appellate"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/uzhhorod"},
    {"url": "https://starlit-marzipan-56ef4f.netlify.app/greatberezny"}
]

button_mapping = {
    "📅Перечинський р-н суд": 0,
    "📅Апеляційний суд": 1,
    "📅Ужгородський м-р суд": 2,
    "📅В.Березнянський\nр-н суд": 3
}

callback_mapping = {
    'callback_pr': 0,
    'callback_appel': 1,
    'callback_uz': 2,
    'callback_vb': 3
}

json_files = [
    {"pad": 'data/data_pr.json'},
    {"pad": 'data/data_zka.json'},
    {"pad": 'data/data_ug.json'},
    {"pad": 'data/data_vb.json'}
]
