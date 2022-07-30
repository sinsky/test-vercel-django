pip install -r requirements.txt
python -m pip install --upgrade pip
python manage.py makemigrations
python manage.py migrate jet
python manage.py collectstatic
