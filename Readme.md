# МосПолитех.Расписание
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)


Этот Telegram-бот помогает студентам быстро и удобно получать доступ к расписанию занятий вуза. С его помощью можно легко узнать время и место проведения занятий.

## Требования
- Python >3.9
- Poetry
- PostgreSQL
- Redis

## Как установить

#### Клонировать репозиторий
`git clone https://github.com/artemmmz/mospolytech-tg-bot.git`

#### Перейти в папку с локальным репозиторием
`cd mospolytech-tg-bot`

#### Установить зависимости
`poetry install`

#### Поработать с переменными окружения
`cp example.env .env`

И отредактируйте файл со своими переменными

#### Запустить 
`python app/bot.py`


## TODO

- [ ] Сделать подписку на расписание
- [ ] Дописать docstrings
- [ ] Поработать над оптимизацией

Made by Artyom Zlobin

