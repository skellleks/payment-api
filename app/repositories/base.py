from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    def get(self, id: str) -> T | None: ...

    @abstractmethod
    def get_all(self) -> dict[str, T]: ...

    @abstractmethod
    def add(self, id: str, item: T) -> None: ...

    @abstractmethod
    def update(self, id: str, item: T) -> None: ...

    @abstractmethod
    def delete(self, id: str) -> None: ...
