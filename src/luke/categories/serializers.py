from django.contrib.auth.models import User

from rest_framework_json_api import serializers

from .models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class CategorySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_date',
            'last_modified',
            'active',
            'user'
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = (
            'user',
            'title',
            'active'
        )
