from aiogram import types, Bot, Dispatcher, filters, F
import asyncio
from config import TOKEN, ADMIN
from database import Database
from buttons.reply_button import all_users_button
from buttons.reply_button import contact_button_ru
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = Database()

class Reg(StatesGroup):
    name = State()
    number = State()


@dp.message(filters.Command("start"))
async def reg1(message: types.Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя')

@dp.message(Reg.name)
async def reg2(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона', reply_markup=contact_button_ru)

@dp.message(Reg.number)
async def two_three(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Вы прошли регистрацию\nИмя:  {data["name"]}\nНомер:  {data["number"]}", reply_markup=all_users_button)
    await state.clear()

@dp.message(F.text=="Посмотрерть всех пользователей")
async def start_function(message: types.Message):
    db.create_table_users()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name or message.from_user.username
    db.add_user(user_id, user_full_name)
    await message.answer("HELLO")

@dp.message(F.text == "Посмотреть всех пользователей")
async def get_all_users(message: types.Message):
    all_users = db.select_user()
    my_list = []
    for user in all_users:
        my_list.append(f"ID: {user[0]} и Имя: {user[1]}")
    if ADMIN == 880328909:
        await message.answer(f"{"\n".join(my_list)}")
    else:
        await message.answer("You are not ADMIN")




async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())