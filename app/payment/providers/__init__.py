from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @property
    @abstractmethod
    def supported_methods(self) -> list[str]:
        ...


_registry: dict[str, PaymentProvider] = {}


def register_provider(name: str):
    def decorator(cls):
        _registry[name] = cls()
        return cls
    return decorator


def get_provider(name: str) -> PaymentProvider | None:
    return _registry.get(name)


def get_all_providers() -> dict[str, PaymentProvider]:
    return dict(_registry)


import app.payment.providers.provider1  # noqa: E402, F401
import app.payment.providers.provider2  # noqa: E402, F401
