from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import *

app_name = MaterialsConfig.name

router = routers.DefaultRouter()
router.register(r'materials', CourseViewSet, basename='materials')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
] + router.urls
