from urllib.parse import urlencode

from app.models.payment_method import PaymentMethod


class PaymentService:
    @classmethod
    def make_new_payment(
        cls,
        amount: int,
        description: str,
        user_id: int,
        method: PaymentMethod,
        provider: str,
    ) -> str:
        base_url = "https://payment_link.com"

        query_params = {
            "amount": amount,
            "desc": description,
            "user_id": user_id,
            "method": method,
            "provider": provider,
        }

        return f"{base_url}?{urlencode(query_params)}"
