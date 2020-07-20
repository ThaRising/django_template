# Django Backend Template

This is a generic Django backend project, which can
be downloaded using cookiecutter for quick setup.  

For a fullstack project using React / Redux, please
refer to the respective repository.

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
