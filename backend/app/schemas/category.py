from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    restaurant_id: UUID
    name: str
    display_order: int = 0


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
