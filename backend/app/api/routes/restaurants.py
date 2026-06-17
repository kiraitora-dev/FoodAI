from uuid import UUID

from fastapi import APIRouter, Response, status

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.restaurant import RestaurantCreate, RestaurantRead, RestaurantUpdate
from app.services.restaurants import RestaurantService

router = APIRouter()


@router.post("", response_model=RestaurantRead, status_code=status.HTTP_201_CREATED)
async def create_restaurant(
    payload: RestaurantCreate,
    session: DbSession,
    current_user: CurrentUser,
) -> RestaurantRead:
    return await RestaurantService(session).create(current_user, payload)


@router.get("", response_model=list[RestaurantRead])
async def list_restaurants(
    session: DbSession,
    current_user: CurrentUser,
    limit: int = 100,
    offset: int = 0,
) -> list[RestaurantRead]:
    return await RestaurantService(session).list_for_owner(
        current_user,
        limit=limit,
        offset=offset,
    )


@router.get("/{restaurant_id}", response_model=RestaurantRead)
async def get_restaurant(
    restaurant_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
) -> RestaurantRead:
    return await RestaurantService(session).get_owned(current_user, restaurant_id)


@router.patch("/{restaurant_id}", response_model=RestaurantRead)
async def update_restaurant(
    restaurant_id: UUID,
    payload: RestaurantUpdate,
    session: DbSession,
    current_user: CurrentUser,
) -> RestaurantRead:
    return await RestaurantService(session).update(current_user, restaurant_id, payload)


@router.delete("/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_restaurant(
    restaurant_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
) -> Response:
    await RestaurantService(session).delete(current_user, restaurant_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
