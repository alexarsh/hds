# Health Dashboard Service

## Demo

You can see the demo here: [https://health-dashboard-service.tk/](https://health-dashboard-service.tk/)

(login with admin / z5fgmeca)

Health status can be seen here: [https://health-dashboard-service.tk/services/health/](https://health-dashboard-service.tk/services/health/)

Availability can be seen here: [https://health-dashboard-service.tk/services/availability/](https://health-dashboard-service.tk/services/availability/)

## Project status

The project was focused on the working main functionality, unit tests coverage and deployment

Things left to be done are:
1. Each service health check should run in it’s own task. When there are a lot of services to check, the task becomes very large and it's not good.
2. Invoking health check url should have some spinning wheel shown to the user when the UI will be developed
3. Current health check is very primitive and can use additional info from the urls to perform a drill down in dashboards reports, for example.
4. Old health checks should be automatically deleted
5. Every api call has a timeout of 5 seconds. When there will be a lot of services, the timeout, number of gunicorn processes and machine resources should be taken into consideration.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to install the project, you will need:

```
1. Python version ">=3.5"
2. Pip
3. Celery
4. Redis (installed and running)
```

### Installing

Here are step by step install instructions:

```
1. Clone the Project
2. From project dir run: 'pip install -r ./requirements.txt'
3. From project dir run: 'python manage.py migrate'
4. From project dir run: 'python manage.py createsuperuser' (You will need the user to login to django admin)
5. From project dir run: 'python manage.py runserver'
6. Open 'localhost:8000' in your browser, login, add the relevant Services
7. From project dir run: 'celery -A hds worker -l info -B'
```

## Running the tests

In order to run the unit tests, go to the project dir and run:

```
python manage.py test
```

## Built With

* [Django](https://www.djangoproject.com/) - Web framework used
* [Celery](http://www.celeryproject.org/) - For running periodic tasks
* [Redis](https://redis.io/) - As a celery broker

## Authors

* **Arshavski Alexander** - [Sourcerer](https://sourcerer.io/alexarsh)
