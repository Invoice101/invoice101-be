from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    mobile_no = serializers.RegexField(regex=r'^[0-9]{10,15}$', required=True,
                                       error_messages={
                                           'invalid': 'Invalid Mobile Number'
                                       })
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_no', 'name', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", 'id', 'mobile_no']
