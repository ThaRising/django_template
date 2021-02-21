# Django Backend Template

This is a generic Django backend project,
which can be downloaded using cookiecutter
for a quick setup.  

A secret-key will automatically be generated
and placed in the settings once setup
has been completed.  

Clone this repository for local use:  
``cookiecutter <url>.git``  

Install dependencies (requires Poetry):  
``poetry install``

**HEADSUP!**  
Flake8 is required to already be installed
in your local environment.  
This is because Flake8 has to be installed
for each version and inside the base
interpreter.  
As such, it is not included in the Poetry
dependencies.  

Install Flake8:  
``python<version> -m pip install flake8``  
Example:  
``python3.8 -m pip install flake8``

This template includes a 
``.terraform-version`` file.  
If you have Tfenv installed you can 
install the correct Terraform CLI 
version via:  
``tfenv install``

## Features

### Integrated OpenAPI Docs

Auto-generated OpenAPI docs are
available at:  
*/redoc*  

The corresponding schemas,
can be found at:  
*/swagger.json*  
*/swagger.yaml*

### Out of the Box JWT Auth

This project has a customized
version of ``drf-simplejwt``
preconfigured.  
See the root urlconf,
for the respective URL paths.

### Integrated Docker configuration

A complete docker configuration,
for local development and testing,
as well as emulation is included and
documented in the main README file.

### More effective Backend folder structure

This project templates folder structure
was built to allow for imports that your
IDE of choice can recognize without any
additional setup, as well as reasonable
relative imports.  

Additionally, the startapp command has been
overridden to provide a more effective
application folder structure.

You can disable this as well as
the other tweaked management commands
by removing the ``"drizm-django-commons"``
application from ``INSTALLED_APPS``.
