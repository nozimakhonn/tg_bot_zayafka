from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = '7679472078:AAGUqWA-Q_s-M-wNCoEG5Qvm40kFy93Aua0'
channel = '@tns_zayafkalar_kanali'
bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}


@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Zayafka qoldirish' or message.text == '/start':
        await startapp(message)
    elif user_id not in user_data:
        await startapp(message)

    elif 'name' not in user_data[user_id]:
        await ask_phone(message)
    elif 'phone' not in user_data[user_id]:
        await ask_age(message)
    elif 'age' not in user_data[user_id]:
        await total_info(message)


@dp.message(Command("start"))
async def startapp(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    await message.answer(f"Assalomu aleykum!\nIltimos ismingizni kiriting")


async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    name = message.text
    user_data[user_id]['name'] = name
    button = [
        [types.KeyboardButton(text="Raqamni yuborish", request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True, resize_keyboard=True)
    await message.answer("Iltimos telefon raqamingizni yuboring", reply_markup=keyboard)


async def ask_age(message: types.Message):
    user_id = message.from_user.id
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    user_data[user_id]['phone'] = phone
    await message.answer("Iltimos yoshingizni kiriting ")

from telegrambotdatbase import save_user
async def total_info(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    fullname = message.from_user.full_name
    age = message.text
    user_data[user_id]['age'] = age
    message_text = (f"Ismingiz:{user_data[user_id]['name']}\n"
                    f"Telefon raqamingiz: {user_data[user_id]['phone']}\n"
                    f"Yoshingiz: {user_data[user_id]['age']}")
    button = [
        [types.KeyboardButton(text="Zayafka qoldirish")]
    ]
    name = user_data[user_id]['name']
    phone = user_data[user_id]['phone']
    age = user_data[user_id]['age']
    save_user(user_id, username, fullname, name, phone, age)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True, resize_keyboard=True)
    await message.answer(f"Zayafka qabul qilindi!\n{message_text}", reply_markup=keyboard)
    await bot.send_message(channel, f"Yangi zayafka!\n{message_text}")
    print(user_data)
    del user_data[user_id]
    print(user_data)


async def main():
    await dp.start_polling(bot)
asyncio.run(main())