from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from modules.config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)