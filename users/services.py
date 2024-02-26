import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_sessions(instance):
    """Функия создлания сессии для оплаты  с помощью сервиса Stripe"""
    product_name = instance.title

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
        # customer_email=f'{}',
    )
    return sessions




