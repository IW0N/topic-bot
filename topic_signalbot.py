from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from modules.tunnels import Tunnels
from modules.messages import MESSAGES
from modules.bot_cmds import *
about_btn=InlineKeyboardButton("Какую проблему решает?", callback_data='about')
about_keyboard=InlineKeyboardMarkup().add(about_btn)

how_to_use_btn=InlineKeyboardButton("Как это использовать?",callback_data='how it to use')
how_to_use_kb=InlineKeyboardMarkup().add(how_to_use_btn)

class topic_signalbot:
    def __init__(self):
        self.__tunnels=Tunnels()
    def __get_topic_id(self,msg:Message):
        return msg.message_thread_id

    async def init_tunnel(self,msg: Message):
        topic_id=self.__get_topic_id(msg)
        chat_id=msg.chat.id
        tunnels=self.__tunnels
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
    def __get_tunnel_id(self,args:str):
    
        try:
            _args=args.replace(" ","")
            return int(_args)
        except:
            return None
    async def connect_to_tunnel(self,msg:Message):
        chat_id=msg.chat.id
        args=msg.get_args()
        tunnels=self.__tunnels
        to_thread=False
        thread_id=msg.message_thread_id
        if thread_id==None:
            hasnt_connection=tunnels.chat_hasnt_connection(chat_id)
            if hasnt_connection:
                tunnel_id=self.__get_tunnel_id(args)
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
        else:
            text="Это должна быть группа, а не топик!"
            to_thread=True
        if to_thread:
            await send_to_topic(text,msg.chat.id,thread_id)
        else:
            await send_msg(chat_id,text)
    async def process_any_msg(self,msg:Message):
        chat_id=msg.chat.id
        topic_id=self.__get_topic_id(msg)
        tunnels=self.__tunnels

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
    async def help(self,msg:Message):
        topic_id=self.__get_topic_id(msg)
        chat_id=msg.chat.id
        text=MESSAGES["help"]
        await send_to_topic(text,chat_id,topic_id)
    async def about(self,msg:Message,mode="about"):
        topic_id=self.__get_topic_id(msg)
        chat_id=msg.chat.id
        text=""
        reply_markup=None
        if mode=="about":
            text=MESSAGES["about"]
            reply_markup=how_to_use_kb
        elif mode=="how it to use":
            text=MESSAGES["how it to use"]
            reply_markup=about_keyboard

        await send_to_topic(text,chat_id,topic_id,reply_markup=reply_markup)