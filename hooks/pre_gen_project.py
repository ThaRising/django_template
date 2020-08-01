import re
import sys

"""
Structure of this tuple is:
(variable_value, [validation_regexes])
"""

validation = [
    ("{{cookiecutter.project_name}}", [r"^[a-zA-Z].*"])
]


def validate_input_values(val_in: list) -> bool:
    for validation_parameter in val_in:
        value, regexes = validation_parameter
        for regex in regexes:
            if not re.match(regex, value, re.MULTILINE):
                return False
    return True


if __name__ == '__main__':
    if not validate_input_values(validation):
        print("The last specified value did not pass validation")
        sys.exit(1)
    sys.exit(0)
