from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository[Order]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Order)

    async def list_for_restaurant(self, restaurant_id: UUID, limit: int = 100, offset: int = 0) -> list[Order]:
        result = await self.session.execute(
            select(Order)
            .where(Order.restaurant_id == restaurant_id)
            .order_by(Order.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())
