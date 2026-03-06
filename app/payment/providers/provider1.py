from app.models.payment_method import PaymentMethod
from app.payment.providers import PaymentProvider, register_provider


@register_provider("provider1")
class Provider1(PaymentProvider):

    @property
    def supported_methods(self) -> list[PaymentMethod]:
        return [PaymentMethod.CARD, PaymentMethod.SBP]
