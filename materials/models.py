from django.db import models
from conf_my import NULLABLE
from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    """Модель Курса"""
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    amount = models.PositiveIntegerField(default=1000, verbose_name='цена')
    updated = models.DateTimeField(**NULLABLE, verbose_name='дата и время обновления')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    """Модель Урока"""
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')
    link = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    amount = models.PositiveIntegerField(default=1000, verbose_name='цена')
    updated = models.DateTimeField(auto_now=True, **NULLABLE)

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='курс')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f"{self.user_id} {self.course_id}"
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
