from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class EmailAuthSerializer(serializers.Serializer):  # noqa
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=True,
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password
            )
            if not user:
                msg = _("Unable to login with provided credentials")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password" fields')
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs
