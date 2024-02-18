from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer

from users.permisions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """Набор представлений для курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода "создание": добавляем сохранение владельца"""
        new_course = serializer.save(owner=self.request.user)
        new_course.save()

    def get_permissions(self):
        """Набор permissions для курса"""
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ('update', 'retrieve'):
            self.permission_classes = [IsAuthenticated, IsModer | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = []
        return super().get_permissions()

class LessonCreateAPIView(generics.CreateAPIView):
    """Представление для создания занятия"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        """Переопределение метода "создание": сохраняем владельца в БД"""
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Представление для просмотра всех занятий"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    """Представление для редактирования занятия"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Представление для просмотра 1 занятия"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModer]

class LessonDeleteAPIView(generics.DestroyAPIView):
    """Представление для удаления 1 занятия"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
