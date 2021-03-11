KeyUA WSGI Application

## Production 
- set production configuration in .env file

``docker-compose up -d``

## Set up project for local development
- Required system packages
```
sudo apt install python3-dev mysql-server libmysqlclient-dev
```

- For set up MySQL use this guide:
[How to install MySQL on Ubuntu](https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru)
  
- Create venv
```
python3 -m  venv venv
```

- Install libs and apply migrations

````
source venv/bin/activate/
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
````

- Also install RabbitMQ server for celery:
```
sudo apt-get install -y erlang
sudo apt-get install rabbitmq-server
```

- Then start and test it:
```
systemctl enable rabbitmq-server
systemctl start rabbitmq-server
systemctl status rabbitmq-server
```
- For RabbitMQ [admin control panel](http://localhost:15672) you must enable plugin:
```
rabbitmq-plugins enable rabbitmq_management
```

``
celery -A keyua1_1 worker --beat -l INFO
``
**Or**
``
sh local_celerybeat.sh
``

- Run server
``python manage.py runserver ``
  
- Add cities by django [admin](http://localhost:8000/admin)
- Social auth available only by 'localhost' not '127.0.0.1'

  
