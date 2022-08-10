# neo-shop

### Simple online store for Neobis using Python, Django and Django Rest Framework

## How to install
____
### Installation on UNIX-MacOS
- __Clone git repository__
```
git clone https://github.com/nakadzima9/neo-shop.git
```
- __Create virtual environment__
```
python3 -m venv env
```
- __Activate virtual environment__
```
source env/bin/activate
```

### Installation on Windows
- __Clone git repository__
```
git clone https://github.com/nakadzima9/neo-shop.git
```
- __Create virtual environment__
```
py -m venv env
```
- __Activate virtual environment__
```
.\env\Scripts\activate
```
- __Installation dependencies__
```
pip install -r requirements.txt
```

- __Database setup__
```
python manage.py makemigrations
python manage.py migrate 
``` 

## Docker
```
docker-compose build
docker-compose run
```
- __Create database and user__
```
docker exec -t neoshop_db
su postgres
CREATE DATABASE neoshop;
CREATE USER neoshop_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE neoshop TO neoshop_admin;
```
- __Running migrations__
```
docker-compose run --rm neoshop python manage.py migrate
```
- __Creating a super user__
```
docker-compose run --rm neoshop python manage.py createsuperuser
```

---
## Built With 🛠️
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)

### Heroku app => **[Link](https://neo-shop.herokuapp.com/)**

### Postman collections soon