# Простой сайт-блог "Blog"


### Использованный стек:

- Python3
- Django
- Materialize (свои шрифты)
- PostgreSQL
- Git



```sh
$ git clone https://github.com/hsolo0999/blog.git
$ cd blog
$ pip install -r requirements.txt

```

#### Варианты запуска:

- В 'debug' режиме
- С использованием вашей базы данных

Для запуска в 'debug' режиме (используется встроенная база данных):

В файле blog_project/constants.py установите значение переменной DEBUG в 'True' (DEBUG = True), затем выполните

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```
Для запуска с использованием вашей базы данных, в файле blog_project/constants.py установите значение переменной DEBUG в 'False' (DEBUG = False), введите данные для подключения вашей **PostrgeSQL** базы данных     
            DBNAME - Имя базы
            DBUSER = Имя пользователя базы
            DBPASSWORD = Пароль
            DBHOST = Хост
            DBPORT = Порт

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```

#### Сайт имеет 2 страницы:

- Главная
- Создание статьи

#### На главной странице 2 рабочие ссылки:

- Блог (все статьи)
- Создать статью
