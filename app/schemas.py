from pydantic import BaseModel

from app.models.payment_method import PaymentMethod


class CreatePaymentRequest(BaseModel):
    plan_id: str
    user_id: int
    method: PaymentMethod
    provider: str


class CreatePaymentResponse(BaseModel):
    payment_url: str


class PlanResponse(BaseModel):
    plan_id: str
    name: str
    duration_months: int
    amount: int
    description: str


class ProviderResponse(BaseModel):
    name: str
    methods: list[str]
