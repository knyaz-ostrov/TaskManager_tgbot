from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from data.scripts.bot_data import BotMessageText, BotCommands
from database.db_shell import DBActions



router = Router()



# Состояние, при котором бот ожидает от пользователя текстовое
# название нового task'а для занесения его в БД
class InputWaiting(StatesGroup):
    input_waiting = State()



@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(BotMessageText.start)



# Команда добавить новый task
@router.message(Command(BotCommands.add_task))
async def add_cmd(message: Message, state: FSMContext) -> None:
    await message.answer(BotMessageText.add_task)
    await state.set_state(InputWaiting.input_waiting)



# Команда получить список всех своих task'ов
@router.message(Command(BotCommands.get_tasks))
async def get_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    tasks = DBActions(message.from_user.username, message.from_user.id).get_tasks()

    mes = ''
    for i, task in enumerate(tasks, 1):
        mes += f'\n{i}. {task}'

    if len(mes) == 0:
        mes = BotMessageText.task_list_empty

    await message.answer(mes)



# Команда полностью очистить список своих task'ов
@router.message(Command(BotCommands.clear_tasks))
async def clear_tasks_cmd(message: Message, state: FSMContext) -> None:
    await state.clear()

    DBActions(message.from_user.username, message.from_user.id).clear_tasks()

    await message.answer(BotMessageText.clear_tasks)



# Получение текстового сообщения с названием нового task'а
@router.message(StateFilter(InputWaiting.input_waiting), F.text)
async def task_creation(message: Message, state: FSMContext) -> None:

    DBActions(message.from_user.username, message.from_user.id).add_task(message.text)

    await message.answer(BotMessageText.task_created)
    await state.clear()
