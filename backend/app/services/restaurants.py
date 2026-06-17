from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.restaurant import Restaurant
from app.models.user import User
from app.repositories.restaurants import RestaurantRepository
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate


class RestaurantService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.restaurants = RestaurantRepository(session)

    async def create(self, owner: User, payload: RestaurantCreate) -> Restaurant:
        restaurant = Restaurant(owner_id=owner.id, **payload.model_dump())
        await self.restaurants.add(restaurant)
        await self.session.commit()
        return restaurant

    async def list_for_owner(self, owner: User, limit: int = 100, offset: int = 0) -> list[Restaurant]:
        return await self.restaurants.list_for_owner(owner.id, limit=limit, offset=offset)

    async def get_owned(self, owner: User, restaurant_id: UUID) -> Restaurant:
        restaurant = await self.restaurants.get(restaurant_id)
        if restaurant is None or restaurant.owner_id != owner.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
        return restaurant

    async def update(self, owner: User, restaurant_id: UUID, payload: RestaurantUpdate) -> Restaurant:
        restaurant = await self.get_owned(owner, restaurant_id)
        for key, value in payload.model_dump(exclude_unset=True).items():
            setattr(restaurant, key, value)
        await self.session.commit()
        await self.session.refresh(restaurant)
        return restaurant

    async def delete(self, owner: User, restaurant_id: UUID) -> None:
        restaurant = await self.get_owned(owner, restaurant_id)
        await self.restaurants.delete(restaurant)
        await self.session.commit()
