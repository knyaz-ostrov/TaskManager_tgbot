# Task Manager Telegram Bot
Телеграм-бот для создания и хранения личного списка задач.
___
> ## Установка (Windows)
У вас должны быть установлены [зависимости проекта](https://github.com/knyaz-ostrov/TaskManager_tgbot#Зависимости)
1. Клонирование репозитория

    `git clone https://github.com/knyaz-ostrov/TaskManager_tgbot.git`

2. Переход в директорию проекта TaskManager_tgbot

    `cd TaskManager_tgbot`

3. Открыть config.json и внести все необходимые данные

    > Путь: `data/data/`
    > 
    > Рекомендую использовать редактор [Notepadd++](https://notepad-plus-plus.org/ "Официальный сайт")

4. Создание виртуального окружения

    `py -m venv env`

5. Активация виртуального окружения

    * cmd -> `call env/Scripts/activate`
   
    * PowerShell -> `env/Scripts/activate`

6. Установка зависимостей

    `pip install -r requirements.txt`

7. Запуск скрипта для создания базы данных

    `py RecreateDB.py`

8. Запуск бота

    `py Bot.py`
___
> ## Поддержка
По любым вопросам, проблемам или предложениям создайте [обсуждение](https://github.com/knyaz-ostrov/TaskManager_tgbot/issues/new/choose) в данном репозитории или напишите мне в [Телеграм](https://t.me/knyaz_ostrov "t.me/knyaz_ostrov") или на почту <knyaz.ostrov@gmail.com>.
___
> ## Зависимости
Эта программа тестировалась на интерпретаторе [Python](https://www.python.org/ "Официальный сайт") версии 3.11.8, PIP 24.0, [PostgreSQL](https://www.postgresql.org/ "Официальный сайт") 16, системе контроля версий [Git](https://git-scm.com/downloads "Официальный сайт") 2.44.0.windows.1.
> ОС:
> 
> Выпуск	Windows 11 Pro
> 
> Версия	23H2

Если вы заметили, что данное ПО можно запустить на версии ниже, или оно не работает на какой-либо версии, то напишите в [поддержку](https://github.com/knyaz-ostrov/TaskManager_tgbot#Поддержка).
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
> ## Контакты для сотрудничества:
* ### Telegram: [t.me/knyaz_ostrov](https://t.me/knyaz_ostrov "https://t.me/knyaz_ostrov")
* ### Email: <knyaz.ostrov@gmail.com>
