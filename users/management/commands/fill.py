from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments

class Command(BaseCommand):
    """Команда для заполнения БД уроками и курсами"""

    def handle(self, *args, **options):

        courses_list = [
            {'title': 'Английский'},
            {'title': 'Немецкий'},
            {'title': 'Испанский'}
        ]

        lessons_list = [
            {'title': '1 Занятие'},
            {'title': '2 занятие'},
            {'title': '3 Занятие'}
        ]

        for courses_item in courses_list:
            Course.objects.create(**courses_item)

        for lessons_item in lessons_list:
            Lesson.objects.create(**lessons_item)

        payments_list = [
            {'course': Course.objects.get(pk=1), 'amount': 100000, 'method': Payments.ChoicePayment.CASH},
            {'course': Course.objects.get(pk=2), 'amount': 50000, 'method': Payments.ChoicePayment.TRANSFER},
            {'course': Course.objects.get(pk=3), 'amount': 50000, 'method': Payments.ChoicePayment.TRANSFER},

            {'lesson': Lesson.objects.get(pk=1), 'amount': 2000, 'method': Payments.ChoicePayment.TRANSFER},
            {'lesson': Lesson.objects.get(pk=3), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
            {'lesson': Lesson.objects.get(pk=2), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
        ]

        for payments_item in payments_list:
            Payments.objects.create(**payments_item)
