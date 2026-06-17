from uuid import UUID

from fastapi import APIRouter, Response, status

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.menu_item import MenuItemCreate, MenuItemRead, MenuItemUpdate
from app.services.menu_items import MenuItemService

router = APIRouter()


@router.post("", response_model=MenuItemRead, status_code=status.HTTP_201_CREATED)
async def create_menu_item(
    payload: MenuItemCreate,
    session: DbSession,
    current_user: CurrentUser,
) -> MenuItemRead:
    return await MenuItemService(session).create(current_user, payload)


@router.get("", response_model=list[MenuItemRead])
async def list_menu_items(
    restaurant_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
    limit: int = 100,
    offset: int = 0,
) -> list[MenuItemRead]:
    return await MenuItemService(session).list_for_restaurant(
        current_user,
        restaurant_id,
        limit=limit,
        offset=offset,
    )


@router.get("/{item_id}", response_model=MenuItemRead)
async def get_menu_item(
    item_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
) -> MenuItemRead:
    return await MenuItemService(session).get_owned(current_user, item_id)


@router.patch("/{item_id}", response_model=MenuItemRead)
async def update_menu_item(
    item_id: UUID,
    payload: MenuItemUpdate,
    session: DbSession,
    current_user: CurrentUser,
) -> MenuItemRead:
    return await MenuItemService(session).update(current_user, item_id, payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu_item(
    item_id: UUID,
    session: DbSession,
    current_user: CurrentUser,
) -> Response:
    await MenuItemService(session).delete(current_user, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
