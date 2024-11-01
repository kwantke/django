
py -m venv .venv

call .venv\Scripts\activate.bat

pip install -r requirements.txt

python manage.py migrate

set DJANGO_SUPERUSER_USERNAME=admin
set DJANGO_SUPERUSER_EMAIL=admin@example.com
set DJANGO_SUPERUSER_PASSWORD=password

python manage.py createsuperuser --noinput