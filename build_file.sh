pip install -r requirements.txt
python3 -m pip install --upgrade pip
python3 manage.py makemigrations
python3 manage.py migrate jet
python3 manage.py collectstatic
