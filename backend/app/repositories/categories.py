from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Category)

    async def list_for_restaurant(
        self,
        restaurant_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Category]:
        result = await self.session.execute(
            select(Category)
            .where(Category.restaurant_id == restaurant_id)
            .order_by(Category.display_order.asc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
