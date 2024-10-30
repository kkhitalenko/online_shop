# online_shop

<details>
   <summary>Запуск проекта локально</summary> 

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:kkhitalenko/online_shop.git
```

```
cd online_shop/backend/
```

Активировать виртуальное окружение и установить зависимости:

```
poetry shell
```
```
poetry install
```

Выполнить миграции:

```
python manage.py migrate
```

Создать суперпользователя:
```
python manage.py createsuperuser
```

Запустить проект:

```
python manage.py runserver
```

</details>

Документация проекта и примеры запросов-ответов к API находится по адресу (при запуске на локальном сервере):

```
http://127.0.0.1:8000/swagger/
```

Используемые технологии: Python, Django, DRF, Swagger