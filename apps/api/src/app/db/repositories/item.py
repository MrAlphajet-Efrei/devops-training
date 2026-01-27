from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import Item
from app.models.item import ItemCreate, ItemUpdate


class ItemRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self, limit: int = 100, offset: int = 0) -> tuple[list[Item], int]:
        total = self.db.scalar(select(func.count()).select_from(Item))
        items = list(
            self.db.scalars(
                select(Item)
                .order_by(Item.created_at.desc())
                .limit(limit)
                .offset(offset)
            )
        )
        return items, total or 0

    def get_by_id(self, item_id: UUID) -> Item | None:
        return self.db.get(Item, item_id)

    def create(self, item_in: ItemCreate) -> Item:
        item = Item(**item_in.model_dump())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item_id: UUID, item_in: ItemUpdate) -> Item | None:
        item = self.get_by_id(item_id)
        if item is None:
            return None
        update_data = item_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(item, key, value)
        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item_id: UUID) -> bool:
        item = self.get_by_id(item_id)
        if item is None:
            return False
        self.db.delete(item)
        self.db.commit()
        return True
