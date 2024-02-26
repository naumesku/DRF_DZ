from django.contrib.auth.models import AbstractUser
from django.db import models

from conf_my import NULLABLE
from datetime import date

from materials.models import Lesson, Course


class User(AbstractUser):
    """Модель класса User"""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    town = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активация пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

class Payments(models.Model):
    """Модель класса Payments"""
    class ChoicePayment(models.TextChoices):
        CASH = 'cash', 'наличные'
        TRANSFER = 'transfer', 'перевод на счет'

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    date = models.DateField(default=date.today, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(choices=ChoicePayment.choices, default='cash', verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
