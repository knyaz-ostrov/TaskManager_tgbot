"""
Модуль с параметрами запуска бота.
"""
import json
import logging

from aiogram import Bot, Dispatcher

from logger import logger
from handlers import general_router, task_manager_router


logger(logging.INFO)


with open('configs/bot.json', encoding='UTF-8') as file:
    token = json.load(file)['token']


bot = Bot(token)


dp = Dispatcher()
dp.include_routers(general_router, task_manager_router)
