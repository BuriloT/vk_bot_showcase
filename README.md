# vk_bot_showcase

## Чат-бот витрина в VK

> Витрина выпечки/кондитерской. 3-4 раздела, в каждом по 2-3 товара. У товара описание и фотография. Из раздела можно возвращаться назад. Для навигации использовать кнопки.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- Vk_api — интерфейс для взаимодействия с VK.
- SQLAlchemy — библиотека  для работы с реляционными СУБД.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BuriloT/vk_bot_showcase.git
```

```
cd vk_bot_showcase
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте и заполните файл .env:

```
VK_TOKEN=YOUR_TOKEN
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
```

Запустите проект:

```
python main.py
```
