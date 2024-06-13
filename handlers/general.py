"""
Модуль содержит в себе хандлеры для выполнения действий в соответствии с событиями, которые ловит
бот.
"""
import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter

from database import PSQLUser
from handlers.misc.data import MessageText
from handlers.misc.states import InputWaiting
from handlers.misc.constants import CMD_ADD_TASK, CMD_GET_TASKS, CMD_CLEAR_TASKS, LOG_TEMPLATE,\
    LOG_TYPE_HANDLER, LOG_MESSAGE_LEN


router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    """
    Стартовая команда.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, start_cmd.__name__, message.from_user.username,\
                  message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    await state.clear()
    await message.answer(MessageText().start)


@router.message(Command(CMD_ADD_TASK))
async def add_task_cmd(message: Message, state: FSMContext) -> None:
    """
    Команда для добавления новой задачи в БД.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, add_task_cmd.__name__,
                  message.from_user.username, message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    await message.answer(MessageText().add_task)
    await state.set_state(InputWaiting.input_waiting)


@router.message(Command(CMD_GET_TASKS))
async def get_tasks_cmd(message: Message, state: FSMContext) -> None:
    """
    Команда для запроса списка своих задач.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, get_tasks_cmd.__name__,
                  message.from_user.username, message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    await state.clear()

    tasks = PSQLUser(message).get_tasks()

    if len(tasks) == 0:
        mes = MessageText().task_list_empty
    else:
        mes = tasks

    await message.answer(mes)


@router.message(Command(CMD_CLEAR_TASKS))
async def clear_tasks_cmd(message: Message, state: FSMContext) -> None:
    """
    Команда для полного удаления списка своих задач из БД.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, clear_tasks_cmd.__name__,
                  message.from_user.username, message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    await state.clear()

    PSQLUser(message).clear_tasks()

    await message.answer(MessageText().clear_tasks)


@router.message(StateFilter(InputWaiting.input_waiting), F.text)
async def task_creation(message: Message, state: FSMContext) -> None:
    """
    Получение текстового сообщения с названием добавляемой задачи.
    """
    logging.debug(LOG_TEMPLATE, LOG_TYPE_HANDLER, task_creation.__name__,
                  message.from_user.username, message.from_user.id, message.text[:LOG_MESSAGE_LEN])

    PSQLUser(message).add_task(message.text)

    await message.answer(MessageText().task_created)
    await state.clear()
