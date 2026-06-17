from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.models.user import User
from app.repositories.orders import OrderRepository
from app.schemas.order import OrderCreate
from app.services.restaurants import RestaurantService


class OrderService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.orders = OrderRepository(session)
        self.restaurants = RestaurantService(session)

    async def create(self, owner: User, payload: OrderCreate) -> Order:
        await self.restaurants.get_owned(owner, payload.restaurant_id)
        order = Order(**payload.model_dump())
        await self.orders.add(order)
        await self.session.commit()
        return order

    async def list_for_restaurant(
        self,
        owner: User,
        restaurant_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Order]:
        await self.restaurants.get_owned(owner, restaurant_id)
        return await self.orders.list_for_restaurant(
            restaurant_id,
            limit=limit,
            offset=offset,
        )
