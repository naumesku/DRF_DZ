from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from config.settings import AUTH_USER_MODEL

from conf_my import NULLABLE
from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для Урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]

class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для Курса"""

    lesson_cnt = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, required=False)
    is_payments = serializers.SerializerMethodField()

    def get_lesson_cnt(self, instance):
        return instance.lesson_set.all().count()

    def get_is_payments(self, instance):
        return Payments.objects.filter(course=instance).exists()

    class Meta:
        model = Course
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для Подписки"""
    is_subscript = serializers.SerializerMethodField()

    def get_is_subscript(self, obj):
        """Проверка существования подписки"""
        subs_item = Subscription.objects.all().filter(user=AUTH_USER_MODEL, course=obj.pk)
        if subs_item.exsist():
            return True
        return False
    class Meta:
        model = Subscription
        fields = '__all__'
