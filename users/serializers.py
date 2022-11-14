from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomTokenObtainPairView(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token