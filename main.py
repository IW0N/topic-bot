from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
import asyncio


from modules.config import TOKEN
from modules.messages import MESSAGES
from modules.bot_cmds import *
from modules.tunnels import Tunnels


chat_for_forward=-1001951815141
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
tunnels=Tunnels()
command_is_working = False

commands=['init_tunnel','get_topic_info','start','bind']
print('Бот запущен!')
def get_topic_id(msg:Message):
    return msg.message_thread_id

@dp.message_handler(commands = ['init_tunnel'])
async def init_tunnel(msg: Message):
    topic_id=get_topic_id(msg)
    chat_id=msg.chat.id
    if topic_id!=None:
        tunnel_id=tunnels.get_tunnel_id(chat_id,topic_id)
        if tunnel_id==None:
            tunnel_id=tunnels.init_tunnel(chat_id,topic_id)
            text=MESSAGES['init_tunnel'].format(tunnel_id)
        else:
            text=f"Тунель уже существует\nId: <code>{tunnel_id}</code>"
        await send_to_topic(text,chat_id,topic_id)
    else:
        await send_msg(chat_id,"Тунель может быть инициализирован только в треде (топике) и только членом СДР!")


def get_tunnel_id(args:str):
    
    try:
        _args=args.replace(" ","")
        return int(_args)
    except:
        return None
@dp.message_handler(commands = ['bind'])
async def connect_to_tunnel(msg:Message):
    chat_id=msg.chat.id
    args=msg.get_args()
    hasnt_connection=tunnels.chat_hasnt_connection(chat_id)
    if hasnt_connection:
        tunnel_id=get_tunnel_id(args)
        if tunnel_id != None:
            tunnel_exists=tunnels.tunnel_exists(tunnel_id)
            if tunnel_exists:
                tunnel_employing=tunnels.tunnel_employing(tunnel_id)
                if not tunnel_employing:
                    tunnels.connect_to_tunnel(tunnel_id,chat_id)
                    text=MESSAGES["bind"]
                else:
                    text="Тоннель уже используется другим чатом!"
            else:
                text="Указываемого тунеля не существует!"
        else:
            text="Некорректный id тунеля. Он должен быть представлен в числовом формате.\nПожалуйста, введите ещё раз"
    else:
        text="Чат уже привязан!"
    await bot.send_message(chat_id,text)


@dp.message_handler()
async def process_any_msg(msg:Message):
    chat_id=msg.chat.id
    topic_id=get_topic_id(msg)
    
    if topic_id==None:
        distance=tunnels.get_root_chat(chat_id)
    else:
        distance=tunnels.get_freelance_chat(chat_id,topic_id)
    if isinstance(distance,tuple):
        (dist_chat_id,dist_topic_id)=distance
    else:
        dist_chat_id=distance
        dist_topic_id=None

    if dist_chat_id!=None:
        await msg.forward(dist_chat_id,dist_topic_id)
    

    
if __name__ == '__main__':
    executor.start_polling(dp)