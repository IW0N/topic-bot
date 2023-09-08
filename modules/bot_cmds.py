'''Модуль с командами для бота'''

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from typing import Callable

from modules.config import TOKEN

def bot_setup(func: Callable):
    '''
    Обёртка с подключением и отключением сесии бота
    '''
    async def wrapper(*args, **kwargs):
        bot = Bot(token=TOKEN)
        dp = Dispatcher(bot)
        await func(*args, **kwargs, dp=dp)
        session = await bot.get_session()
        await session.close()
    return wrapper

@bot_setup
async def send_msg(user_id: int, text: str, dp: Dispatcher | None=None, **kwargs):
    '''Отправка сообщения'''
    await dp.bot.send_message(user_id, text, parse_mode='html', **kwargs)
@bot_setup
async def send_to_topic(text:str,topic_chat_id:int,topic_id:int, dp: Dispatcher | None=None, **kwargs):
    await dp.bot.send_message(topic_chat_id,text,parse_mode="html",reply_to_message_id=topic_id,**kwargs)
@bot_setup
async def forward_msg(chat_id_to: int, chat_id_from: int, msg_id: int, dp: Dispatcher | None=None, **kwargs):
    '''Пересылка сообщения'''
    await dp.bot.forward_message(chat_id_to, chat_id_from, msg_id, **kwargs)