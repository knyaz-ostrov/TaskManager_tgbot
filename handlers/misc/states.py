"""
Модуль для хранения видов состояний.
"""
from aiogram.fsm.state import StatesGroup, State


class InputWaiting(StatesGroup):
    """
    Класс хранит состояние сценария, при котором пользователь хочет сохранить в базу данных новую
    задачу.
    """
    # Ожидание получения названия задачи.
    input_waiting = State()
