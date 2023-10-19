from modules.root_bot import *
from aiogram.utils import executor
from aiogram.types import Message,CallbackQuery
from topic_signalbot import topic_signalbot

signalbot=topic_signalbot()

print('Бот запущен!')

@dp.message_handler(commands = ['init_tunnel'])
async def init_tunnel(msg: Message):
    await signalbot.init_tunnel(msg)

@dp.message_handler(commands = ['bind'])
async def connect_to_tunnel(msg:Message):
    await signalbot.connect_to_tunnel(msg)

@dp.message_handler(commands=['help'])
async def help(msg:Message):
    await signalbot.help(msg)

@dp.message_handler(commands=['about'])
async def about(msg:Message):
    await signalbot.about(msg)

@dp.callback_query_handler(text="how it to use")
async def process_data(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await signalbot.about(callback_query.message,"how it to use")

@dp.callback_query_handler(text="about")
async def process_data(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await signalbot.about(callback_query.message,"about")
    

@dp.message_handler()
async def process_any_msg(msg:Message):
    await signalbot.process_any_msg(msg)


if __name__ == '__main__':
    executor.start_polling(dp)