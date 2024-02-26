from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Представление для создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Переопределение метода "создание": делаем зарегистрированных пользователей активными"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UserListAPIView(generics.ListAPIView):
    """Представление для просмотра списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdateAPIView(generics.UpdateAPIView):
    """Представление для редактирования пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра 1 пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteAPIView(generics.DestroyAPIView):
    """Представление для удаления 1 пользователя"""
    queryset = User.objects.all()

class PaymentListAPIView(generics.ListAPIView):
    """Набор представлений для платежа"""
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ('date',)

