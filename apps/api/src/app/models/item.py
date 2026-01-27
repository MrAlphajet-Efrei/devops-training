from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    description: str | None = None


class Item(ItemBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ItemListResponse(BaseModel):
    items: list[Item]
    total: int
