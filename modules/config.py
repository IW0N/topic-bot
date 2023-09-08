'''
Модуль для получения конфиг-данных
'''

from json import load

with open('config.json') as file:
    config = load(file)

TOKEN = config.get('token')