from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments

class Command(BaseCommand):
    """Команда для заполнения БД уроками и курсами"""

    def handle(self, *args, **options):
        payments_list = [
            {'user': 1, 'course': Course.objects.get(pk=2), 'amount': 100000, 'method': Payments.ChoicePayment.CASH},
            {'user': 4, 'course': Course.objects.get(pk=3), 'amount': 50000, 'method': Payments.ChoicePayment.TRANSFER},
            {'user': 1, 'lesson': Lesson.objects.get(pk=2), 'amount': 2000, 'method': Payments.ChoicePayment.TRANSFER},
            {'user': 4, 'lesson': Lesson.objects.get(pk=3), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
            {'user': 1, 'lesson': Lesson.objects.get(pk=4), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
        ]

        for payments_item in payments_list:
            Payments.objects.create(**payments_item)

