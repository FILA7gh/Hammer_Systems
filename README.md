# Hammer_Systems

# Приложение реферальной системы

## Старт проекта

Создать .env файл с .env.example ключами из директории config и заполнить их необходимыми значениями.

Установить зависимости:
pip install -r requirements.txt

Активировать виртуальное окружения:
python3 -m venv venv
source venv/bin/activate

Накатить миграции:
python manage.py migrate

Создать суперпользователя для доступа к админке:
python manage.py createsuperuser

Запуск приложения:
python manage.py runserver


## Панель администратора
http://localhost:8000/admin/

# Документация
http://localhost:8000/swagger/