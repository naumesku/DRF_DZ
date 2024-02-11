from django.shortcuts import render
from rest_framework import generics

from materials.models import Lesson
from materials.serializers import LessonSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
