from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menu_item import MenuItem
from app.models.user import User
from app.repositories.menu_items import MenuItemRepository
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate
from app.services.restaurants import RestaurantService


class MenuItemService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.menu_items = MenuItemRepository(session)
        self.restaurants = RestaurantService(session)

    async def create(self, owner: User, payload: MenuItemCreate) -> MenuItem:
        await self.restaurants.get_owned(owner, payload.restaurant_id)
        item = MenuItem(**payload.model_dump())
        await self.menu_items.add(item)
        await self.session.commit()
        return item

    async def list_for_restaurant(
        self,
        owner: User,
        restaurant_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[MenuItem]:
        await self.restaurants.get_owned(owner, restaurant_id)
        return await self.menu_items.list_for_restaurant(restaurant_id, limit=limit, offset=offset)

    async def get_owned(self, owner: User, item_id: UUID) -> MenuItem:
        item = await self.menu_items.get(item_id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found")
        await self.restaurants.get_owned(owner, item.restaurant_id)
        return item

    async def update(self, owner: User, item_id: UUID, payload: MenuItemUpdate) -> MenuItem:
        item = await self.get_owned(owner, item_id)
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(item, key, value)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def delete(self, owner: User, item_id: UUID) -> None:
        item = await self.get_owned(owner, item_id)
        await self.menu_items.delete(item)
        await self.session.commit()
