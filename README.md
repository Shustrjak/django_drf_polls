# POLLSUSER
В данной сборке используются: 

`Django 2.2.10, django-rest-framework`

Создание виртуальной среды:
`$pip install virtualenv {name}`  -- name => Имя виртуальной среды

Активируем вирутальную среду: `source venv/scripts/activate`

Установка зависимостей в виртуальной среде: `install -r requirements_dev.txt`

Создаем project:`django-admin startproject [Название проекта]` """в моем варианте: pollsuser"""

Переходим в проект: `cd [Название проекта]`

Внутри проекта создаем приложение:`python manage.py createapp polls`

####Дополнения в проекте:

---settings.py---


```
INSTALLED_APPS = [
    ...
    'polls',
    'rest_framework',
]
```
---urls.py---
```
urlpatterns += [

    path('polls/', include('polls.urls'))
]
```
Начало API:

[/polls/api/v1/](http://localhost:8000/polls/api/v1/)

Список опросов: 

[http://localhost:8000/polls/api/v1/polls/](http://localhost:8000/polls/api/v1/polls/)

Список вопросов:

[http://localhost:8000/polls/api/v1/questions/](http://localhost:8000/polls/api/v1/questions/)     
список вопросов связанных с опросами.

Список ответов: 

[http://localhost:8000/polls/api/v1/answers/](http://localhost:8000/polls/api/v1/answers/)    
выводится список ответов связанных с вопросами.


В каждой модели присутсвует: вывод списком, детальный вывод, создание модели, изменение модели, удаление модели.

