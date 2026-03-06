from pydantic import BaseModel


class CreatePaymentRequest(BaseModel):
    plan_id: str
    user_id: int
    method: str
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
