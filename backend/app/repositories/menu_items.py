from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menu_item import MenuItem
from app.repositories.base import BaseRepository


class MenuItemRepository(BaseRepository[MenuItem]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, MenuItem)

    async def list_for_restaurant(
        self,
        restaurant_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[MenuItem]:
        result = await self.session.execute(
            select(MenuItem)
            .where(MenuItem.restaurant_id == restaurant_id)
            .order_by(MenuItem.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
