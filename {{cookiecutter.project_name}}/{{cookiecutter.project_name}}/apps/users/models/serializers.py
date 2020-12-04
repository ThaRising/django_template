from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        required=True, validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all()
            )
        ]
    )
    password = serializers.CharField(
        min_length=8,
        max_length=50,
        write_only=True,
        required=True
    )

    def create(self, validated_data):
        model = get_user_model()
        return model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance
