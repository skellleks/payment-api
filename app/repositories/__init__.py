from pathlib import Path
from typing import Type

from app.repositories.base import BaseRepository
from app.repositories.json_repository import JsonRepository


def create_repository(
    storage_type: str,
    entity_cls: Type,
    path: str | Path | None = None,
) -> BaseRepository:
    if storage_type == "json":
        if path is None:
            raise ValueError("'path' is required for json repository")
        return JsonRepository(path=path, entity_cls=entity_cls)
    raise ValueError(f"Unknown storage type: {storage_type}")
