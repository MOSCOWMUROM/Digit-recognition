from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from ChatGPT import gpt

TOKEN = 'TOKEN_TELEGRAM_BOT'
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer('Привет, это чат-бот на основе модели gpt 3.5')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def mes(message: types.Message):
    await message.answer('Генерируется ответ')
    await message.reply(
        gpt(message.text))
    await bot.delete_message(chat_id=message.chat.id,
                             message_id=message.message_id + 1)


if __name__ == '__main__': 
    executor.start_polling(dp)