FROM python:3.9

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /django_app

CMD python manage.py runserver 0.0.0.0:8000
