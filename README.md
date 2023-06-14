## Благотворительный фонд поддержки котов (QRKot)

### 1. [Общая информация о проекте](#1)
### 2. [База данных и переменные окружения](#2)
### 3. [Команды для запуска](#3)
### 4. [Работа с API](#4)
### 5. [Использованные технологии](#5)
### 6. [Об авторе](#6)

---
### 1. Общая информация о проекте <a id=1></a>

Проект MusicMate - это веб-сервис для поиска музыкантами групп и группами музыкантов. Главная 
страница представляет собой ленту, содержимое которой зависит от вида пользователя, вошедшего в систему.
Если вход совершил пользователь "музыкант", то лента будет отображать ему объявления групп,
если вход совершил пользователь "группа (ансамбль)", то в ленте будут видны объявления
музыкантов.
- при регистрации необходимо выбрать вид пользователя - "группа" или "музыкант"
- чтобы получить возможность общаться, пользователи должны сделать взаимный отклик
друг на друга (по аналогии с match в приложениях знакомств)
- после взаимного отклика становится доступен функционал личных сообщений
- также на сервисе есть форум, с возможностью создания тематических разделов и подразделов

---
### 2. База данных и переменные окружения <a id=2></a>

under construction

---
### 3. Команды для запуска <a id=3></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Invictus-7/music_mate
```

Создать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Windows: source venv/Scripts/activate
```

Обновить pip и установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python manage.py makemigrations
```

Запустить проект:
```bash
python manage.py runserver
```

После запуска проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/)  
Документация по API проекта доступна можно по адресам:
  - Swagger: [http://localhost:8000/api/v1/schema/docs/](http://localhost:8000/api/v1/schema/docs/)

---
### 4. Работа с API <a id=4></a>

#### В проекте MusicMate имеются следующие эндпоинты:
```
under construction

```

#### Примеры запросов:
- Получение всех объявлений:
```
under construction

```

- Создание объявления:
```
under construction

```

- Создание темы на форуме:
```
under construction

```
---
### 5. Использованные технологии <a id=5></a>

- [Python](https://www.python.org/)
- [Django Rest Framework](https://www.djangoproject.com/)
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [dfr-spectacular](https://alembic.sqlalchemy.org/en/latest/)

---
### 6. Об авторе <a id=6></a>
- [Кирилл Резник](https://github.com/Invictus-7)