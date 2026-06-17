from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.models.user import User
from app.repositories.categories import CategoryRepository
from app.schemas.category import CategoryCreate
from app.services.restaurants import RestaurantService


class CategoryService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.categories = CategoryRepository(session)
        self.restaurants = RestaurantService(session)

    async def create(self, owner: User, payload: CategoryCreate) -> Category:
        await self.restaurants.get_owned(owner, payload.restaurant_id)
        category = Category(**payload.model_dump())
        await self.categories.add(category)
        await self.session.commit()
        return category

    async def list_for_restaurant(
        self,
        owner: User,
        restaurant_id: UUID,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Category]:
        await self.restaurants.get_owned(owner, restaurant_id)
        return await self.categories.list_for_restaurant(
            restaurant_id,
            limit=limit,
            offset=offset,
        )
