from django.urls import path
from users.views import *
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-detale'),
    path('create/', UserCreateAPIView.as_view(), name='user-detale'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detale'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    path('payment_create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
