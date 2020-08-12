from django.urls import path
from rest_framework import routers
from .views import ObtainTokenView


router = routers.SimpleRouter()

urlpatterns = [
    path("login/", ObtainTokenView.as_view())
]

urlpatterns += router.urls
