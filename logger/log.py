"""
Модуль для настроек логгирования.
"""
import logging

from logger.constants import LOG_FILE_PATH, LOG_FORMAT


def logger(level: int) -> None:
    """
    Задаёт параметры логгирования.
    
    :param level: Уровень логирования.
    :return:
    """
    logging.basicConfig(
        level=level,
        filename=LOG_FILE_PATH,
        filemode="a",
        format=LOG_FORMAT,
        encoding='UTF-8'
    )
