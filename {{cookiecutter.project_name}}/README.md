# {{cookiecutter.project_name}}

This project was generated with
the Cookiecutter CLI,
using the **Drizm-Django-Template**.

## Setup

If you generated this project,
then all the actions listed below,
will have already automatically
been performed.

Otherwise,
you will need to add a file for
all the project related secrets.

To file is expected to be located at
``{{cookiecutter.project_name}}/settings/keys.py``

You must add the following variables:  
- SECRET_KEY = 'your-secret-key-here'

For your convinience, these are
used during local development.

You will however, have to add them
as environment variables for deployment.

## Development

To get started with local development,
run the following commands for a
quick setup:  
````bash
cd docker
docker-compose up --build
poetry run python manage.py migrate
poetry run python manage.py runserver
````

This project includes a default
superuser.  
The development credentials are:  
- Email: "root@root.com"
- Password: "root"

You can change these in the
development settings file.

## Local Deployment

To set up a local, dockerized
testing environment, do the following:  
````bash
cd docker
docker-compose -f docker-compose.yml -f docker-compose.srv.yml up --build --force-recreate
````

## Deployment

This file includes a full
setup for a pipeline
from development to Heroku.

If you do not wish to use this,
you can remove the following:  
- Profile
- runtime.txt
- The package "dj-database-url" from the dependencies

The following environment
variables need to be set
for deployment:
- SECRET_KEY
- ADMIN_EMAIL
- ADMIN_PASSWORD