from app.payment.providers import PaymentProvider, register_provider


@register_provider("provider2")
class Provider2(PaymentProvider):

    @property
    def supported_methods(self) -> list[str]:
        return ["sbp"]
