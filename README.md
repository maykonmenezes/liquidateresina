# Liquida Teresina (Campanha do Varejo de Teresina)


> Version: 1.0


## Description



## Requirements
### Core

* Python (3.6.6 used) - https://www.python.org/
* Django (2.2.6) - https://www.djangoproject.com/



## Set up the application

Install Python dependencies:

    pip install -r requirements.txt

Create migrations of the models:

    python manage.py makemigrations liquida2018

Apply migrations to the database:

    python manage.py migrate

Run the server:

    python manage.py runserver



## Running Tests

You can run some automated tests to check the functionalities by running the command below:

    python manage.py liquida2018.tests
