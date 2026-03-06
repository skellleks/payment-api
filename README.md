# Payment API

Проект построен на FastAPI с многослойной архитектурой: **models -> repositories -> services -> routers**.

- **Repository** - абстрактный `BaseRepository[T]` с JSON-реализацией. При необходимости легко заменить хранилище на БД, добавив новую реализацию.
- **Service** - бизнес-логика и валидация, работает с репозиторием через абстракцию.
- **Provider Registry** - платёжные провайдеры подключаются через декоратор `@register_provider`, каждый провайдер - отдельный класс.

Для простоты база данных не используется - тарифные планы хранятся в `plans.json`.

**Добавление нового провайдера:** создать файл в `app/payment/providers/`, унаследовать `PaymentProvider`, реализовать `supported_methods` и зарегистрировать через декоратор.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Или
```bash
docker compose up -d
```

Документация API: http://localhost:8000/docs
