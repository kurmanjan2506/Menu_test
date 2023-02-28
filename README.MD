Для запуска выполните следующие команды:
1. ~ git clone git@github.com:kurmanjan2506/Menu_test.git
2. ~ python3 -m venv venv
3. ~ . venv/bin/activate
4. ~ pip install -r requirements.txt
5. Заполните .env по env_example
6. Создайте базу данных в postgres
7. ~ ./manage.py makemigrations
8. ~ ./manage.py migrate
9. ~ ./manage.py createsuperuser
10. ~ ./manage.py runserver

Для запуска докера выполните следующие команды:
1. Зайдите в .env и поменяйте DB_HOST=localhost на DB_HOST=db 
2. ~ docker-compose built
3. ~ docker-compose run web ./manage.py createsuperuser
4. ~ docker-compose up
