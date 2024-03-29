SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    "DEFAULT_AUTO_SCHEMA_CLASS":
        "{{cookiecutter.project_name}}.lib.openapi_schema_gen.ReadWriteAutoSchema",
}

__all__ = ["SWAGGER_SETTINGS"]
