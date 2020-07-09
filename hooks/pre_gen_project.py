import secrets

context = {{cookiecutter}}  # noqa

context["secret_key"] = secrets.token_hex()  # noqa
