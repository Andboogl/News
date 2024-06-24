# News
News - це новинний сайт на Python з використанням веб фреймворку Django. Ви, наприклад, можете використовувати його для сайту сімейних новин.

# Запуск
## macOS & Linux
pip install -r requirements.txt<br>
cd app<br>
python3 manage.py makemigrations<br>
python3 manage.py migrate<br>
python3 manage.py createsuperuser<br>
python3 manage.py

## Windows
pip install -r requirements.txt<br>
cd app<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py createsuperuser<br>
python manage.py

#
Зауважте, що ці команди запускають локальний сервер. Для запуску у вашій мережі WiFi у кінці пишете таку команду:

## macOS & Linux

python3 manage.py IP_вашої_мережі_Wifi:Порт

## Windows
python manage.py IP_вашої_мережі_Wifi:Порт