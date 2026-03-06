from fastapi import APIRouter

from app.services.plan_service import plan_service
from app.schemas import PlanResponse

router = APIRouter(prefix="/api/plans", tags=["plans"])


@router.get("/", response_model=list[PlanResponse])
def list_plans():
    return [
        PlanResponse(plan_id=plan_id, **plan.__dict__)
        for plan_id, plan in plan_service.list_plans().items()
    ]
