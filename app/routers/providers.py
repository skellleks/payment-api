from fastapi import APIRouter

from app.schemas import ProviderResponse
from app.payment.providers import get_all_providers

router = APIRouter(prefix="/api/providers", tags=["providers"])


@router.get("/", response_model=list[ProviderResponse])
def list_providers():
    return [
        ProviderResponse(name=name, methods=provider.supported_methods)
        for name, provider in get_all_providers().items()
    ]
