FROM python:3.10

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/

CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT