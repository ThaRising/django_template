import secrets
import sys
from collections import OrderedDict  # noqa

context = {{cookiecutter}}  # noqa

context["secret_key"] = secrets.token_hex()  # noqa

sys.exit(0)
