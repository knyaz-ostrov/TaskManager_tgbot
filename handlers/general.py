from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from scripts.bot_message_text import GetBotMessageText
from scripts.bot_commands import GetBotCommands
from scripts.db_shell import DBMethods as db


router = Router()

class InputWaiting(StatesGroup):
    input_waiting = State()


@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(GetBotMessageText().get_start_message())

@router.message(Command(GetBotCommands().get_add_task_cmd()))
async def add_cmd(message: Message, state: FSMContext) -> None:
    await message.answer(GetBotMessageText().get_add_task_message())
    await state.set_state(InputWaiting.input_waiting)


@router.message(Command(GetBotCommands().get_get_tasks_cmd()))
async def get_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    tasks = db(message.from_user.username, message.from_user.id).get_tasks()

    mes = ''
    for i, task in enumerate(tasks, 1):
        mes += f'\n{i}. {task}'

    if len(mes) == 0:
        mes = GetBotMessageText().get_task_list_empty_message()

    await message.answer(mes)


@router.message(Command(GetBotCommands().get_clear_task_cmd()))
async def clear_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    db(message.from_user.username, message.from_user.id).clear_tasks()
    
    await message.answer(GetBotMessageText().get_clear_tasks_message())


@router.message(StateFilter(InputWaiting.input_waiting), F.text)
async def task_creation(message: Message, state: FSMContext) -> None:

    db(message.from_user.username, message.from_user.id).add_task(message.text)

    await message.answer(GetBotMessageText().get_task_created_message())
    await state.clear()