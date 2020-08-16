from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

from rest_framework_simplejwt.views import (
    TokenObtainPairView as TokenObtainPairView_,
    TokenRefreshView as TokenRefreshView_,
    TokenVerifyView as TokenVerifyView_,
)


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Create Token",
        operation_description="Takes a set of user credentials "
                              "and returns an access and refresh JSON web"
                              "token pair to prove the authentication of "
                              "those credentials.",
        security=[]
    )
)
class TokenObtainPairView(TokenObtainPairView_):
    pass


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Create Refresh Token",
        operation_description="Takes a refresh type JSON web token "
                              "and returns an access type JSON web token "
                              "if the refresh token is valid.",
        security=[]
    )
)
class TokenRefreshView(TokenRefreshView_):
    pass


@method_decorator(
    name="post", decorator=swagger_auto_schema(
        operation_summary="Verify Token",
        operation_description="Takes a token and indicates if it is valid."
                              " This view provides no information "
                              "about a token's fitness for a particular use.",
        security=[]
    )
)
class TokenVerifyView(TokenVerifyView_):
    pass
