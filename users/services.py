import stripe
from config.settings import STRIPE_API_KEY
from materials.models import Course, Lesson

stripe.api_key = STRIPE_API_KEY

def create_sessions(instance):
    """Функия создлания сессии для оплаты  с помощью сервиса Stripe"""
    print('instance= ', instance)


    product_name = Course.objects.all().filter(pk=instance.course_id) if instance.course else Lesson.objects.all().filter(pk=instance.lesson_id)
    print('product_name= ', product_name)

    # Создание продукта
    product = stripe.Product.create(name=f'{product_name.title}')

    # Создание цены
    price = stripe.Price.create(
        currency="usd",
        unit_amount=instance.amount,
        recurring={"interval": "month"},
        product_data={"name": product.id},
    )

    # Создание сессии
    sessions = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": f'{price.id}', "quantity": 1}],
        mode="payment",
        customer_email=f'{instance.user.email}',
    )
    return sessions





