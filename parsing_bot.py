from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello World")

# /news

executor.start_polling(dp)