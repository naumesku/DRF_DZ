from celery import shared_task
import datetime
from users.models import User

@shared_task
def check_active_users():
    """Меняет пользователям не заходившим на сайт более 30 дней поле is_active на False"""

    # user = User.objects.get(id=5) # Получаем пользователя, которого хотим обновить
    # user.last_login = timezone.now() - datetime.timedelta(days=30) # Устанавливаем новое значение для поля last_login
    # user.save() # Сохраняем изменения

    User.objects.filter(
        is_active=True,
        last_login__lte=datetime.datetime.now() - datetime.timedelta(days=30)
        ).update(is_active=False)
