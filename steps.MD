Create folder for project
git init
create folder project/app
cd project/app
python3 -m venv .venv/
pip install Django==5.0
pip install gunicorn
create Dockerfile.local

```
FROM python:3.10.6
WORKDIR /usr/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/app/requirements.txt 
RUN chmod +x /usr/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /usr/app/

CMD ["python", "/usr/app/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
```

go to project folder
create docker-compose file

```
#./django-docker/docker-compose.yml
version: '0.1'

services:
  web:
    build:
         context: ./app 
         dockerfile: Dockerfile.local
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./app/:/usr/app/
    ports:
      - 4000:8000
    env_file:
      - ./env/django.env
```

Create the folder env/
go to folder env/
create file django.env and populate with variables for django


Then modofy the settings.py file as follows:
```
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", default="forlocaltest")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=1))

APP_NAME = os.environ.get("FLY_APP_NAME")
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ") if os.environ.get('ALLOWED_HOSTS') else ['localhost', '127.0.0.1','*',f"{APP_NAME}.fly.dev
```

docker compose up --build