from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

all_users_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть всех пользователей")]
])

contact_button_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Поделиться контактом", request_contact=True)]
])