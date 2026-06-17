from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MenuItemBase(BaseModel):
    restaurant_id: UUID
    category_id: UUID | None = None
    name: str
    description: str | None = None
    price: Decimal
    currency: str = "USD"
    dietary_tags: list[str] = []
    allergens: list[str] = []
    calories: int | None = None
    is_available: bool = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    category_id: UUID | None = None
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    currency: str | None = None
    dietary_tags: list[str] | None = None
    allergens: list[str] | None = None
    calories: int | None = None
    is_available: bool | None = None


class MenuItemRead(MenuItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
