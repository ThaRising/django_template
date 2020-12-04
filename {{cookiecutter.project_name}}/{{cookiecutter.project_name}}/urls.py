from django.contrib import admin
from django.urls import path, include, re_path
from .docs.openapi import schema_view
from django.conf import settings
from django.views.generic.base import RedirectView
from .apps.users.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # Included URL paths
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    # Note that eh browsable API auth is absent,
    # because it uses SessionAuth, while we use JWT
    re_path(r'^favicon\.ico$', favicon_view),

    # JWT Token-Auth endpoints
    path(
        'tokens/',
        include(
            '{{cookiecutter.project_name}}.apps.tokens.urls',
            namespace="tokens"
        )
    ),

    # User defined URL paths
]

# Add the DebugToolbar only in development mode
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
