# Решение тестовой задачи
Стек технологий использованный в проекте: Python 3, Django 2.2.16, Stripe 

Автор:
- [Борис Сенкевич](https://github.com/basyna)

 - Протестировать решение, выложенное в контейнере Docker можно по адресу: [158.160.20.111:8000](158.160.20.111:8000/item/01)

## Задание
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price) 
API с двумя методами:
 - GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
 - GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy.


### Примеры использования
```
  - curl -X GET http://localhost:8000/item/1
```
 - Возвращает HTML c инфой и кнопкой Buy. По нажатию на кнопку Buy происходит запрос на _/buy/{id}_, получение session_id и далее  с помощью JS библиотеки Stripe происходит редирект на Checkout форму

```
  - curl -X GET http://localhost:8000/buy/1
```
 - При выполнении этого метода c бэкенда с помощью python библиотеки stripe выполняется запрос stripe.checkout.Session.create(...) и полученный _session.id_ выдаваться в результате запроса

## Как запустить проект:
Клонировать репозиторий:

```
- git clone git@github.com:Filimon4ik2/api_yamdb.git
```
Установить и активировать виртуальное окружение:

```
python -m venv venv
. venv/Scripts/activate
```

Установить необходимые зависимости requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Создаем суперпользователя, если нужно:

```
python manage.py createsuperuser
```
Для работы необходимо создать файл _.env_ в корне проекта с ключами доступа к Stripe (котоорые нужно получить на сайте) и Django:
```
SK_TEST_KEY = sk_test_51M5B
PK_TEST_KEY = pk_test_51M5B
SECRET_KEY = 'django-insecur

```
Запустить проект:
```
python manage.py runserver
```
