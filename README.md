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
  <h3 align="left">● Run "py Bot.py"
