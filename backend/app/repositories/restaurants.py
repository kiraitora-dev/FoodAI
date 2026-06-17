from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.restaurant import Restaurant
from app.repositories.base import BaseRepository


class RestaurantRepository(BaseRepository[Restaurant]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Restaurant)

    async def list_for_owner(
        self,
        owner_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Restaurant]:
        result = await self.session.execute(
            select(Restaurant)
            .where(Restaurant.owner_id == owner_id)
            .order_by(Restaurant.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
