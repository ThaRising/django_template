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
- ``SECRET_KEY = 'your-secret-key-here'``

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
docker-compose -p {{cookiecutter.project_name | lower}} \
  -f docker-compose.yml \
  -f docker-compose.vols.yml \
  up --build
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
docker-compose -p {{cookiecutter.project_name | lower}} \
  -f docker-compose.yml \
  -f docker-compose.vols.yml \
  -f docker-compose.srv.yml \
  up --build
````

The server should now be
available at ``localhost:8080``.

You may get an error saying
``"Permission denied ... postgres-data"``.  
in that case you simply need to run
``rm -rf ./postgres-data``.

This will however clear
all data from previous runs,
so you may instead want to
run the docker-compose command
as a superuser via for example ``sudo``.

## Testing

To run local tests,
you will need to first start
all the required docker-compose
services.

To make this process easier,
a script for this is included,
called ``pre_test.sh``.

You can simply run this before
you run the actual tests, like so:
````bash
bash ./tests/pre_test.sh
poetry run python manage.py test ./tests
````

To finish your test session,
simply destroy all the leftover
services like so:
````bash
docker-compose -p {{cookiecutter.project_name | lower}}tests \
  down --volumes
````

## Deployment

This project includes a full
setup for a pipeline
from development to Heroku.

If you do not wish to use this,
you can remove the following:  
- Procfile
- runtime.txt
- The package "dj-database-url" from the dependencies

The following environment
variables need to be set
for deployment:
- ``DJANGO_SETTINGS_MODULE``
- ``SECRET_KEY``
- ``ADMIN_EMAIL``
- ``ADMIN_PASSWORD``

Finally, run ``make requirements``,
to compile the ``requirements.txt`` file.
