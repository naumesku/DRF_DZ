from celery import shared_task
import datetime
from users.models import User

@shared_task
def check_active_users():
    """Меняет пользователям не заходившим на сайт более 30 дней поле is_active на False"""

    User.objects.filter(
        is_active=True,
        last_login__lte=datetime.datetime.now() - datetime.timedelta(days=30)
        ).update(is_active=False)
