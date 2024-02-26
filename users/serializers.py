from rest_framework import serializers
from users.models import User, Payments
# from users.services import create_sessions


class PaymentsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payments"""
    # link_payments = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = '__all__'

    # def get_link_payments(self, instance):
    #     return create_sessions(instance)

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
