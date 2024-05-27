from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from data.scripts.bot_data import BotMessageText
from data.scripts.bot_data import BotCommands
from database.db_shell import DBMethods



router = Router()



class InputWaiting(StatesGroup):
    input_waiting = State()



@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(BotMessageText().get_start())



@router.message(Command(BotCommands().get_add_task()))
async def add_cmd(message: Message, state: FSMContext) -> None:
    await message.answer(BotMessageText().get_add_task())
    await state.set_state(InputWaiting.input_waiting)



@router.message(Command(BotCommands().get_get_tasks()))
async def get_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    tasks = DBMethods(message.from_user.username, message.from_user.id).get_tasks()

    mes = ''
    for i, task in enumerate(tasks, 1):
        mes += f'\n{i}. {task}'

    if len(mes) == 0:
        mes = BotMessageText().get_task_list_empty()

    await message.answer(mes)



@router.message(Command(BotCommands().get_clear_tasks()))
async def clear_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    DBMethods(message.from_user.username, message.from_user.id).clear_tasks()
    
    await message.answer(BotMessageText().get_clear_tasks())



@router.message(StateFilter(InputWaiting.input_waiting), F.text)
async def task_creation(message: Message, state: FSMContext) -> None:

    DBMethods(message.from_user.username, message.from_user.id).add_task(message.text)

    await message.answer(BotMessageText().get_task_created())
    await state.clear()