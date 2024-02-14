from rest_framework import serializers
from materials.models import Course, Lesson
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lesson_cnt = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)
    def get_lesson_cnt(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
