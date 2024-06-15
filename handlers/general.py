"""
Модуль содержит в себе базовые хандлеры.
"""
import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from handlers.misc.data import MessageText
from handlers.misc.constants import LOG_TEMPLATE, LOG_TYPE_HANDLER, LOG_MESSAGE_LEN


general_router = Router()


@general_router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    """
    Стартовая команда.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, start_cmd.__name__, message.from_user.username,\
                  message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    await state.clear()
    await message.answer(MessageText().start)
