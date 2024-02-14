from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments

class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {'course': Course.objects.get(pk=2), 'amount': 100000, 'method': Payments.ChoicePayment.CASH },
            {'course': Course.objects.get(pk=3), 'amount': 50000, 'method': Payments.ChoicePayment.TRANSFER},
            {'lesson': Lesson.objects.get(pk=2), 'amount': 2000, 'method': Payments.ChoicePayment.TRANSFER},
            {'lesson': Lesson.objects.get(pk=3), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
            {'lesson': Lesson.objects.get(pk=4), 'amount': 2000, 'method': Payments.ChoicePayment.CASH},
        ]

        for payments_item in payments_list:
            Payments.objects.create(**payments_item)

