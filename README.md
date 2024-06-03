# Task Manager & Template Telegram Bot
Телеграм-бот для создания и хранения личного списка задач.
#
## Установка (Windows)
У вас должны быть установлены ЗАВИСИМОСТИ ПРОЕКТА
1. Клонирование репозитория

    `git clone https://github.com/knyaz-ostrov/TaskManager_tgbot.git`

2. Переход в директорию TaskManager_tgbot

    `cd TaskManager_tgbot`

3. Создание виртуального окружения

    `py -m venv env`

4. Активация виртуального окружения

    ● cmd -> `call env/Scripts/activate`
   
    ● PowerShell -> `env/Scripts/activate`

5. Установка зависимостей

    `pip install -r requirements.txt`

6. Запуск скрипта для создания базы данных

    `py RecreateDB.py`

7. Запуск бота

    `py Bot.py`
#
## Поддержка
По любым вопросам, проблемам или предложениям создайте [обсуждение](https://github.com/knyaz-ostrov/TaskManager_tgbot/issues/new/choose) в данном репозитории или напишите мне в [Телеграм](https://t.me/knyaz_ostrov).
#
## Зависимости
Эта программа зависит от интерпретатора Python версии 3.11.8 или выше, PIP 24.0 или выше, PostgreSQL 16 или выше. Если вы заметили, что данное ПО можно запустить на версии ниже, или оно не работает на какой-либо версии, то напишите в [поддержку](https://github.com/knyaz-ostrov/TaskManager_tgbot#Поддержка).
#
##








<h1 align="left">Телеграм-бот для ведения личного списка задач;
  <h1 align="center">Шаблон бота для будущих проектов;
    <h1 align="right">Демонстрация навыков.
      
<h1 align="left">Python 3.11.8v
  
<h2 align="left">Frameworks:
  
  <h3 align="left">Default:
  <h4 align="left">● asyncio
  <h4 align="left">● logging
  <h4 align="left">● json
    
  <h3 align="left">Installed:
  <h4 align="left">● aiogram
  <h4 align="left">● psycopg2
  <h4 align="left">● lxml
    
<h2 align="left">Description:
<h4 align="left">Простой телеграм-бот, имеющий на борту, помимо стартовой, три команды:
  <h3 align="left">● /add - добавить задачу
  <h3 align="left">● /tsk - показать список личных задач
  <h3 align="left">● /clr - удалить все личные задачи
    
<h4 align="left">Для хранения списка задач используется PostgreSQL.
  
<h4 align="left">Текстовые сообщения бота и команды, которые он воспринимает хранятся в XML-файле:
  <h3 align="left">● "data/data/bot_data.xml"
    
<h4 align="left">Конфиги (токен бота, данные для подключения к БД) должны быть предварительно записаны в JSON-файл:
  <h3 align="left">● "data/data/config.json"

<h2 align="left">Running:
  <h3 align="left">● Предварительно необходимо создать и развернуть виртуальное окружение
  <h3 align="left">● Далее следует установить все зависимости из файла "requirements.txt"
  <h3 align="left">● Заполнить файл конфигурации актуальными параметрами
  <h3 align="left">● Установить и настроить PostgreSQL, если всё ещё не сделали это
  <h3 align="left">● Развернуть базу данных: "py RecreateDB.py"
  <h3 align="left">● Run "py Bot.py"
