from django.db import models
from conf_my import NULLABLE

class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(**NULLABLE, verbose_name='описание')
    link = models.URLField(**NULLABLE, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

