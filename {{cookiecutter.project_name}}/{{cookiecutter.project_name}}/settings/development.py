from .production import *  # noqa
from .keys import *  # noqa

DEBUG = True

ADMIN_EMAIL = 'root@root.com'
ADMIN_PASSWORD = 'root'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'default',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': os.getenv('DJANGO_DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

MIDDLEWARE = [
    {% if cookiecutter.cors_integration|int %}
    # Activate CORS
    'corsheaders.middleware.CorsMiddleware',
    {% endif %}

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    {% if cookiecutter.cors_integration|int %}
    # Let all CSRF checks pass that pass CORS
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    {% endif %}

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

{% if cookiecutter.cors_integration|int %}
CORS_ALLOW_ALL_ORIGINS = True
CORS_REPLACE_HTTPS_REFERER = True
{% endif %}

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = [
    "127.0.0.1"
]
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')
