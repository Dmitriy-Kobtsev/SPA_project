import stripe
from conf.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создаем продукт в страйпе"""

    return stripe.Product.create(name=product)


def create_stripe_price(product, amount):
    """
    Создание цены в страйпе
    :param product:
    :param amount:
    :return:
    """

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product_data={"name": product.get("id")},
    )


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get("id"), session.get("url")
