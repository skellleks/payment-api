from pathlib import Path

from app.models.plan import SubscriptionPlan
from app.repositories import create_repository
from app.repositories.base import BaseRepository


class PlanService:

    def __init__(self, repository: BaseRepository[SubscriptionPlan]):
        self._repository = repository

    def get_plan(self, plan_id: str) -> SubscriptionPlan | None:
        return self._repository.get(plan_id)

    def list_plans(self) -> dict[str, SubscriptionPlan]:
        return self._repository.get_all()

    def add_plan(self, plan_id: str, plan: SubscriptionPlan) -> None:
        self._validate(plan)
        self._repository.add(plan_id, plan)

    def update_plan(self, plan_id: str, plan: SubscriptionPlan) -> None:
        self._validate(plan)
        self._repository.update(plan_id, plan)

    def delete_plan(self, plan_id: str) -> None:
        self._repository.delete(plan_id)

    @staticmethod
    def _validate(plan: SubscriptionPlan) -> None:
        if not plan.name or not plan.name.strip():
            raise ValueError("Plan name must not be empty")
        if plan.duration_months <= 0:
            raise ValueError("Duration must be greater than 0")
        if plan.amount <= 0:
            raise ValueError("Amount must be greater than 0")


_plan_repository = create_repository(
    storage_type="json",
    entity_cls=SubscriptionPlan,
    path=Path(__file__).resolve().parent.parent.parent / "plans.json",
)

plan_service = PlanService(_plan_repository)
