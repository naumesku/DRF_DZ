from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_message_about_update(users: list, name_materials, title):
    """Функция отправки сообщений об обновлоении пользователям, подписанным на материал"""
    subject = f'{name_materials} обновлен.'
    message = f'{name_materials} {title} обновлен. Посмотрите изменения'
    print("Сообщение: ", message)

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users,
    )
