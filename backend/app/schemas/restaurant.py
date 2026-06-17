from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RestaurantBase(BaseModel):
    name: str
    description: str | None = None
    address: str | None = None
    phone: str | None = None
    cuisine_type: str | None = None
    is_active: bool = True


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    address: str | None = None
    phone: str | None = None
    cuisine_type: str | None = None
    is_active: bool | None = None


class RestaurantRead(RestaurantBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    owner_id: UUID
