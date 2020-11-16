from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView as __TokenObtainPairView,
    TokenRefreshView as __TokenRefreshView,
    TokenVerifyView as __TokenVerifyView,
)

from .models.serializers import (
    CustomTokenObtainPairSerializer,
    ObtainSchema,
    RefreshSchema
)


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Create Token",
        operation_description="Takes a set of user credentials "
                              "and returns an access and refresh JSON web"
                              "token pair to prove the authentication of "
                              "those credentials.",
        security=[],
        responses={
            status.HTTP_200_OK: ObtainSchema(),
            status.HTTP_401_UNAUTHORIZED: "Invalid Credentials"
        }
    )
)
class TokenObtainPairView(__TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Request new Token",
        operation_description="Takes a refresh type JSON web token "
                              "and returns an access type JSON web token "
                              "if the refresh token is valid.",
        security=[],
        responses={
            status.HTTP_200_OK: RefreshSchema(),
            status.HTTP_401_UNAUTHORIZED: "Refresh token invalid"
        }
    )
)
class TokenRefreshView(__TokenRefreshView):
    pass


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Verify Token",
        operation_description="Takes a token and indicates if it is valid."
                              " This view provides no information "
                              "about a token's fitness for a particular use.",
        security=[],
        responses={
            status.HTTP_200_OK: "Access token valid",
            status.HTTP_401_UNAUTHORIZED: "Access token invalid"
        }
    )
)
class TokenVerifyView(__TokenVerifyView):
    pass
