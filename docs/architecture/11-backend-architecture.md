# 11. Backend Architecture

## 11.1 Application Structure

```
apps/api/src/app/
├── main.py                 # FastAPI application entry
├── config.py               # Settings (Pydantic)
├── api/
│   ├── router.py           # Main router
│   ├── deps.py             # Dependencies (DB session)
│   └── routes/
│       ├── health.py
│       └── items.py
├── models/                 # Pydantic schemas
├── db/
│   ├── session.py          # SQLAlchemy session
│   ├── models.py           # ORM models
│   └── repositories/       # Data access layer
├── services/               # Business logic
└── middleware/             # Custom middleware
```

## 11.2 Application Factory

```python
# src/app/main.py
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

def create_app() -> FastAPI:
    app = FastAPI(title="DevOps Learning API", version="1.0.0")

    # Middleware
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins)
    app.add_middleware(RequestLoggingMiddleware)

    # Prometheus
    Instrumentator().instrument(app).expose(app, endpoint="/metrics")

    # Routes
    app.include_router(api_router)

    return app

app = create_app()
```

## 11.3 Repository Pattern

```python
# src/app/db/repositories/item.py
class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, limit: int, offset: int) -> tuple[list[ItemModel], int]:
        total = self.db.scalar(select(func.count(ItemModel.id)))
        items = list(self.db.scalars(
            select(ItemModel).order_by(ItemModel.created_at.desc()).limit(limit).offset(offset)
        ).all())
        return items, total or 0

    def create(self, item_in: ItemCreate) -> ItemModel:
        item = ItemModel(name=item_in.name, description=item_in.description)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
```

## 11.4 Configuration

```python
# src/app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "devops_demo"
    db_user: str = "app_user"
    db_password: str
    debug: bool = False
    cors_origins: list[str] = ["http://localhost:3000"]

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()
```

---
