from app.models.payment_method import PaymentMethod
from app.payment.providers import PaymentProvider, register_provider


@register_provider("provider2")
class Provider2(PaymentProvider):
    @property
    def supported_methods(self) -> list[PaymentMethod]:
        return [PaymentMethod.SBP]
