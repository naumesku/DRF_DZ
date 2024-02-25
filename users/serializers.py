from rest_framework import serializers
from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payments"""

    class Meta:
        model = Payments
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
