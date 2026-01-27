from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.db.repositories.item import ItemRepository
from app.models.item import Item, ItemCreate, ItemListResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["items"])


def _get_repo(db: Session = Depends(get_db)) -> ItemRepository:
    return ItemRepository(db)


@router.get("", response_model=ItemListResponse)
def list_items(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    repo: ItemRepository = Depends(_get_repo),
) -> ItemListResponse:
    items, total = repo.get_all(limit=limit, offset=offset)
    return ItemListResponse(items=items, total=total)


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(
    item_in: ItemCreate,
    repo: ItemRepository = Depends(_get_repo),
) -> Item:
    return repo.create(item_in)


@router.get("/{item_id}", response_model=Item)
def get_item(
    item_id: UUID,
    repo: ItemRepository = Depends(_get_repo),
) -> Item:
    item = repo.get_by_id(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


@router.put("/{item_id}", response_model=Item)
def update_item(
    item_id: UUID,
    item_in: ItemUpdate,
    repo: ItemRepository = Depends(_get_repo),
) -> Item:
    item = repo.update(item_id, item_in)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: UUID,
    repo: ItemRepository = Depends(_get_repo),
) -> None:
    if not repo.delete(item_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
