
Запуск первого проекта сайта

django-admin startproject coolsite

после запуска в терминале, появилась папка coolsite

cd coolsite

далее запустим тестовый сервер

python manage.py runserver

появился файл db.sqlite3 , можно в дальнейшем изменить программу базы данных на другую
из поддерживаемых PostgreSQL, MatiaDB, MySQL, Oracle и SQLite

Иногда после изменений нужно перезапустить сервер
Quit the server with CTRL-BREAK (закрываем сервер сочетаниями клавиш CTRL-BREAK )
и снова запускаем
python manage.py runserver

Запуск сервера с другим портом (по умолчанию  http://127.0.0.1:8000/)
python manage.py runserver 4000
или
python manage.py runserver 192.168.1.1:5000 (на локальном компьютере это не сработает, нужно для другого и так для справки)
