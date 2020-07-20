# Django Backend Template

This is a generic Django backend project,
which can be downloaded using cookiecutter
for quick setup.  

Clone this repository for local use:  
``cookiecutter <url>.git``

View help for the included Makefile:  
``make``  

HEADSUP!  
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
If you have Tfenv installed you install
the correct Terraform CLI version via:  
``tfenv install``

Auto-generated OpenAPI docs are
available at:  
/redoc  

The corresponding schemas can be found at:  
/swagger.json  
/swagger.yaml
