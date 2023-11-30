## Начало работы

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Rocksed/Django-and-Stripe.git
cd Django-and-Stripe
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения:

    Создайте файл .env в корне проекта и добавьте в него следующее:

    STRIPE_PUBLIC_KEY=your_stripe_public_key
    STRIPE_SECRET_KEY=your_stripe_secret_key

    Замените your_stripe_public_key и your_stripe_secret_key на ваши API-ключи Stripe.

4. Запустите миграцию:
```bash
python manage.py migrate
```

5. Загрузка фикстур в базу данных(Если необходима загрузить тестовые данные)
```bash
python manage.py loaddata item.json
```
6. Создание суперпользователя(Для доступа к django admin)
```bash
python manage.py createsuperuser
```

7. Запустите сервер:
```bash
python manage.py runserver
    Посетите http://localhost:8000 в веб-браузере.
```

## Использование

    Перейдите на страницу с описанием товара: http://localhost:8000/item/1/.
    Нажмите кнопку "Купить", чтобы начать процесс оплаты.
    Перейдите на страницу с описанием товара: http://localhost:8000/buy/1/ для получения session_id