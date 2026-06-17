from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OrderItem(BaseModel):
    item_id: UUID
    quantity: int
    name: str
    price: Decimal


class OrderBase(BaseModel):
    restaurant_id: UUID
    customer_name: str | None = None
    status: str = "pending"
    items: list[OrderItem]
    subtotal: Decimal
    currency: str = "USD"


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
