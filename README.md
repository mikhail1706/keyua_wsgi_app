# KeyUA WSGI Application

### Setup local development server

#### MySql server:

- use this guide [How to install MySQL on Ubuntu](https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru)

#### RabbitMQ server for celery:

- ```sudo apt-get install -y erlang```
- ```sudo apt-get install rabbitmq-server```

#### Then start and test it:
- ```systemctl enable rabbitmq-server```
- ```systemctl start rabbitmq-server```
- ```systemctl status rabbitmq-server```

#### For RabbitMQ [admin control panel](http://localhost:15672) you must enable the plugin:
- ``rabbitmq-plugins enable rabbitmq_management``

#### Create .env file based on .env.example

- ``cp .evn.example .env``

#### Define settings in .env file for local development

#### Create environment, install required packages and apply migrations
- ``python3 -m  venv venv``
- ``source venv/bin/activate/``
- ``pip install --upgrade pip``
- ``pip install -r requirements.txt``
- ``python manage.py migrate``

#### Run server 
- ``python manage.py runserver``

#### Run celery worker and beat
- ``celery -A keyua_wsgi_app worker --beat -l INFO`` or ``sh local_celerybeat.sh``

#### Some addition information

- Add cities by django [admin](http://localhost:8000/admin)
- Social auth available only by 'localhost' not '127.0.0.1'

### Production server


#### Docker

- ``docker-compose build``
- ``docker-compose up -d``
  
