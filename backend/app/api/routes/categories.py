from uuid import UUID

from fastapi import APIRouter

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.category import CategoryCreate, CategoryRead
from app.services.categories import CategoryService

router = APIRouter()


@router.post("", response_model=CategoryRead, status_code=201)
async def create_category(
    payload: CategoryCreate,
    session: DbSession,
    current_user: CurrentUser,
) -> CategoryRead:
    return await CategoryService(session).create(current_user, payload)


@router.get("", response_model=list[CategoryRead])
async def list_categories(
    restaurant_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
    limit: int = 100,
    offset: int = 0,
) -> list[CategoryRead]:
    return await CategoryService(session).list_for_restaurant(
        current_user,
        restaurant_id,
        limit=limit,
        offset=offset,
    )
