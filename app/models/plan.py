from dataclasses import dataclass


@dataclass(frozen=True)
class SubscriptionPlan:
    name: str
    duration_months: int
    amount: int
    description: str
