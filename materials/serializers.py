from rest_framework import serializers

from conf_my import NULLABLE
from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lesson_cnt = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, required=False)
    def get_lesson_cnt(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'
