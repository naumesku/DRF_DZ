from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from materials.models import Lesson, Course
from users.models import User


class LessonCRUDTest(APITestCase):
    """Класс проверки механизма CRUD для урока"""
    def setUp(self) -> None:
        self.user = User.objects.create(email='user_test@sky.ru')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test Course'
        )
        self.lesson = Lesson.objects.create(
            title='Test',
            owner=self.user
        )

    def test_get_list_all_lessons(self):
        """Тест просмотра списка уроков"""
        response = self.client.get(
            reverse('materials:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
                    'next': None,
                    'previous': None,
                    'results': [
                            {'id': self.lesson.id,
                             'title': 'Test',
                             'preview': None,
                             'description': None,
                             'link': None,
                             'course': None,
                             'owner': self.user.id}
                    ]
             }
        )

    def test_create(self):
        """Тест создания урока"""

        data = {'title': 'Test',
                'course': self.course.id,
                }

        response = self.client.post(
            reverse('materials:lesson-create'),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {'id': 2,
             'title': 'Test',
             'preview': None,
             'description': None,
             'link': None,
             'course': 1,
             'owner': 1
             }
        )

    def test_updaate(self):
        """Тест обновления урока"""

        lesson_update = Lesson.objects.all().filter(owner_id=self.user).first()
        pk_update = lesson_update.id
        data = {'description': 'Test_description'}
        response = self.client.patch(
                f'/lesson/update/{pk_update}/',
                data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': pk_update,
             'title': 'Test',
             'preview': None,
             'description': 'Test_description',
             'link': None,
             'course': None,
             'owner': self.user.id
             }
        )

    def test_delete_lesson(self):
        """Тест удаление урока"""
        lesson_delete = Lesson.objects.all().filter(owner_id=self.user).first()
        pk_delete = lesson_delete.id
        response = self.client.delete(
                f'/lesson/delete/{pk_delete}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTest(APITestCase):
    """Класс проверки активации подписки"""
    def setUp(self) -> None:
        self.user = User.objects.create(email='user_test@sky.ru')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Test Subscription')
    def test_activate_subscription(self):
        """Тест активации подписки"""

        data = {
            'user_id': self.user.id,
            'course_id': self.course.id
        }

        response = self.client.post(
            reverse('materials:subscription'),
            data=data
        )
        print("response=", response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
