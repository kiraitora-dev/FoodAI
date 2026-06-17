from uuid import UUID

from fastapi import APIRouter, status

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.order import OrderCreate, OrderRead
from app.services.orders import OrderService

router = APIRouter()


@router.post("", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: OrderCreate,
    session: DbSession,
    current_user: CurrentUser,
) -> OrderRead:
    return await OrderService(session).create(current_user, payload)


@router.get("", response_model=list[OrderRead])
async def list_orders(
    restaurant_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
    limit: int = 100,
    offset: int = 0,
) -> list[OrderRead]:
    return await OrderService(session).list_for_restaurant(
        current_user,
        restaurant_id,
        limit=limit,
        offset=offset,
    )
