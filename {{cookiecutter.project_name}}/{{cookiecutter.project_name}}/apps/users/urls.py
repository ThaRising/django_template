from django.urls import path
from rest_framework import routers
from .views import ObtainExpiringTokenView


router = routers.SimpleRouter()

urlpatterns = [
    path("login/", ObtainExpiringTokenView.as_view())
]

urlpatterns += router.urls
