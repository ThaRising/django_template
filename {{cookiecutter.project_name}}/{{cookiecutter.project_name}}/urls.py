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
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^favicon\.ico$', favicon_view),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # User defined URL paths
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
