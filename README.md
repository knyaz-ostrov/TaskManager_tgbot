# Task Manager & Template Telegram Bot
Телеграм-бот для создания и хранения личного списка задач.
___
> ## Установка (Windows)
У вас должны быть установлены [зависимости проекта](https://github.com/knyaz-ostrov/TaskManager_tgbot#Зависимости)
1. Клонирование репозитория

    `git clone https://github.com/knyaz-ostrov/TaskManager_tgbot.git`

2. Переход в директорию с конфигурационным файлом в TaskManager_tgbot

    `cd TaskManager_tgbot/data/data`

3. Открыть config.json и внести все необходимые данные
   
6. Вернуться в корневую папу TaskManager_tgbot

   `cd ../..`

7. Создание виртуального окружения

    `py -m venv env`

8. Активация виртуального окружения

    * cmd -> `call env/Scripts/activate`
   
    * PowerShell -> `env/Scripts/activate`

9. Установка зависимостей

    `pip install -r requirements.txt`

9. Запуск скрипта для создания базы данных

    `py RecreateDB.py`

10. Запуск бота

    `py Bot.py`
___
> ## Поддержка
По любым вопросам, проблемам или предложениям создайте [обсуждение](https://github.com/knyaz-ostrov/TaskManager_tgbot/issues/new/choose) в данном репозитории или напишите мне в [Телеграм](https://t.me/knyaz_ostrov "t.me/knyaz_ostrov").
___
> ## Зависимости
Эта программа зависит от интерпретатора Python версии 3.11.8 или выше, PIP 24.0 или выше, PostgreSQL 16 или выше. Если вы заметили, что данное ПО можно запустить на версии ниже, или оно не работает на какой-либо версии, то напишите в [поддержку](https://github.com/knyaz-ostrov/TaskManager_tgbot#Поддержка).
___
> ## Функционал бота
Кроме стартовой, бот имеет три кастомные команды:
1. Добавить новую задачу

    `/add`

2. Показать список своих задач

    `/tsk`

3. Удалить свои задачи

    `/clr`
___
<h3 align="right"><a href="https://t.me/knyaz_ostrov" title="t.me/knyaz_ostrov">@knyaz_ostrov</a>
