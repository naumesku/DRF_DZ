import stripe
from config.settings import STRIPE_API_KEY
import json
from datetime import datetime, timedelta
from django_celery_beat.models import PeriodicTask, IntervalSchedule

stripe.api_key = STRIPE_API_KEY

def create_sessions(instance):
    """Функия создания сессии для оплаты  с помощью сервиса Stripe"""
    product_name = f"{instance.course_id}" if instance.course_id else f"{instance.lesson_id}"

    # Создание продукта
    product = stripe.Product.create(name=f'{product_name}')

    # Создание цены
    price = stripe.Price.create(
        currency="usd",
        unit_amount=instance.amount,
        product=f'{product.id}',
    )

    # Создание сессии
    sessions = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
        customer_email=f'{instance.user.email}',
    )
    return sessions


def set_schedule(*args, **kwargs):
    """Переодическая задача для celery для старта функции проверки неактивных пользователей."""
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='check_active_users',  # simply describes this periodic task.
        task='users.tasks.check_active_users',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )
