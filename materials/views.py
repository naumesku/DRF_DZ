from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import MaterialsPaginator
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer

from users.permisions import IsModer, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """Набор представлений для курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPaginator

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
    # permission_classes = [AllowAny]
    def perform_create(self, serializer):
        """Переопределение метода "создание": сохраняем владельца в БД"""
        new_lesson = serializer.save(owner=self.request.user)
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Представление для просмотра всех занятий"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MaterialsPaginator

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


class SubscriptionView(APIView):
    """Представление для подписки"""
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course_id")
        course_item = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'

        # Возвращаем ответ в API
        return Response({"message": message})
