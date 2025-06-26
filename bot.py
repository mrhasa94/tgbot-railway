from aiogram import Bot, Dispatcher, executor, types
import logging
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Привет! Я бот и работаю на Railway!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
