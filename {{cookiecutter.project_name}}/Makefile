SHELL := /bin/bash
.DEFAULT_GOAL := requirements

app_src = {{cookiecutter.project_name}}
tests_src = tests

.PHONY: requirements
requirements:
	@poetry export --dev --without-hashes -f requirements.txt > requirements.txt
