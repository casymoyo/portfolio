web: gunicorn casy_portifolio.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
heroku ps:scale web=1
python manage.py migrate