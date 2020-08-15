from datetime import datetime, timedelta

import pytz
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise AuthenticationFailed("User inactive or deleted")

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        expiration_time = settings.DRF_TOKEN_EXPIRATION_TIME

        if token.created < utc_now - timedelta(minutes=expiration_time):
            raise AuthenticationFailed("Token has expired")

        return token.user, token
