from fastapi import APIRouter

from app.dependencies.auth import CurrentUser
from app.dependencies.database import DbSession
from app.schemas.recommendation import (
    ChatRequest,
    ChatResponse,
    NutritionRequest,
    NutritionResponse,
    RecommendationRequest,
    RecommendationResponse,
)
from app.services.recommendations import RecommendationService

router = APIRouter()


@router.post("", response_model=RecommendationResponse)
async def recommend(
    payload: RecommendationRequest,
    session: DbSession,
    current_user: CurrentUser,
) -> RecommendationResponse:
    return await RecommendationService(session).recommend(current_user, payload)


@router.post("/nutrition", response_model=NutritionResponse)
async def nutrition(payload: NutritionRequest, session: DbSession) -> NutritionResponse:
    return await RecommendationService(session).nutrition(payload)


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest, session: DbSession) -> ChatResponse:
    return await RecommendationService(session).chat(payload)
