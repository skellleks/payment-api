import json
from dataclasses import asdict
from pathlib import Path
from typing import TypeVar, Type

from app.repositories.base import BaseRepository

T = TypeVar("T")


class JsonRepository(BaseRepository[T]):
    def __init__(self, path: str | Path, entity_cls: Type[T]):
        self._path = Path(path)
        self._entity_cls = entity_cls
        self._items: dict[str, T] = {}
        self._load()

    def _load(self):
        with open(self._path, encoding="utf-8") as f:
            data = json.load(f)
        self._items = {key: self._entity_cls(**fields) for key, fields in data.items()}

    def _save(self):
        data = {key: asdict(item) for key, item in self._items.items()}
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get(self, id: str) -> T | None:
        return self._items.get(id)

    def get_all(self) -> dict[str, T]:
        return dict(self._items)

    def add(self, id: str, item: T) -> None:
        if id in self._items:
            raise ValueError(f"Item '{id}' already exists")
        self._items[id] = item
        self._save()

    def update(self, id: str, item: T) -> None:
        if id not in self._items:
            raise KeyError(f"Item '{id}' not found")
        self._items[id] = item
        self._save()

    def delete(self, id: str) -> None:
        if id not in self._items:
            raise KeyError(f"Item '{id}' not found")
        del self._items[id]
        self._save()
