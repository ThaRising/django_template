# Django Backend Template

This is a generic Django backend project,
which can be downloaded using cookiecutter
for quick setup.  

A secret-key will automatically be generated
and placed in the settings once setup
has been completed.  

Clone this repository for local use:  
``cookiecutter <url>.git``  

Install dependencies (requires Poetry):  
``poetry install``  

Fetch static files:  
``python manage.py get-media``  

View help for the included Makefile:  
``make``  

**HEADSUP!**  
Flake8 is required to already be installed
in your local environment.  
This is because Flake8 has to be installed
for each version and inside of the base
interpreter.  
As such it is not included in the Poetry
dependencies.  

Install Flake8:  
``python<version> -m pip install flake8``  
Example:  
``python3.8 -m pip install flake8``

This template includes a terraform
version file.  
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

### Ships with a Dockerfile
Coming soon.

### More effective Backend folder structure
This project templates folder structure
was built to allow for imports that your
IDE of choice can recognize without
additional setup, as well as reasonable
relative imports.  

Additionally the startapp command has been
overridden to provide a more effective
application folder structure.  
If you do not want this then you can
delete the modified command, see the section
below for the location of the scripts.

### Custom management commands
These overridden commands are placed
in the "custom" application.

If you want to delete them, either
unregister the "custom" application from
INSTALLED_APPS or delete the folder, or
whichever files you want.

##### get-media
This will download the necessary static
files for the CRISPY_TEMPLATE_PACK
specified.  

It will also automatically generate a
base.html template that includes these
static files.

##### startapp
This command has been overridden to
automatically place your applications in
the correct folder and also includes an
improved default folder structure.
