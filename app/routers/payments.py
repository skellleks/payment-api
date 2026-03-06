from fastapi import APIRouter, HTTPException

from app.services.plan_service import plan_service
from app.services.payment_service import PaymentService
from app.schemas import CreatePaymentRequest, CreatePaymentResponse
from app.payment.providers import get_provider

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.post("/", response_model=CreatePaymentResponse)
def create_payment(request: CreatePaymentRequest):
    plan = plan_service.get_plan(request.plan_id)
    if not plan:
        raise HTTPException(status_code=400, detail="Неизвестный тариф")

    provider = get_provider(request.provider)
    if not provider:
        raise HTTPException(status_code=400, detail="Неизвестный провайдер")

    if request.method not in provider.supported_methods:
        raise HTTPException(
            status_code=400,
            detail=f"Провайдер '{request.provider}' не поддерживает метод '{request.method}'",
        )

    payment_url = PaymentService.make_new_payment(
        amount=plan.amount,
        description=plan.description,
        user_id=request.user_id,
        method=request.method,
        provider=request.provider,
    )

    return CreatePaymentResponse(payment_url=payment_url)
