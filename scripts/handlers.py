from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from misc.data import *
from scripts.db_shell import DBMethods as db


router = Router()

class InputWaiting(StatesGroup):
    input_waiting = State()


@router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    await message.answer(BotMessageText.START_MESSAGE)


@router.message(Command(BotCommands.ADD_TASK))
async def add_cmd(message: Message, state: FSMContext) -> None:
    await message.answer(BotMessageText.ADD_TASK)
    await state.set_state(InputWaiting.input_waiting)


@router.message(Command(BotCommands.GET_TASKS))
async def get_tasks_cmd(message: Message) -> None:

    tasks = db(message.from_user.username, message.from_user.id).get_tasks()

    mes = ''
    for i, task in enumerate(tasks, 1):
        mes += f'\n{i}. {task}'

    if len(mes) == 0:
        mes = BotMessageText.TASK_LIST_EMPTY

    await message.answer(mes)


@router.message(Command(BotCommands.CLEAR_TASKS))
async def clear_tasks_cmd(message: Message) -> None:
    
    db(message.from_user.username, message.from_user.id).clear_tasks()
    
    await message.answer(BotMessageText.CLEAR_TASKS)


@router.message(StateFilter(InputWaiting.input_waiting), F.text)
async def task_creation(message: Message, state: FSMContext) -> None:

    db(message.from_user.username, message.from_user.id).add_task(message.text)

    await message.answer(BotMessageText.TASK_CREATED)
    await state.clear()