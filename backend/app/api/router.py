from fastapi import APIRouter

from app.api.routes import (
    auth,
    categories,
    health,
    menu_items,
    orders,
    recommendations,
    restaurants,
)

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(
    restaurants.router,
    prefix="/restaurants",
    tags=["restaurants"],
)
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(menu_items.router, prefix="/menu-items", tags=["menu-items"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(
    recommendations.router,
    prefix="/recommendations",
    tags=["recommendations"],
)
