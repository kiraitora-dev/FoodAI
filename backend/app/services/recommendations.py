from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recommendation import Recommendation
from app.models.user import User
from app.repositories.recommendations import RecommendationRepository
from app.schemas.recommendation import (
    ChatRequest,
    ChatResponse,
    NutritionRequest,
    NutritionResponse,
    RecommendationRequest,
    RecommendationResponse,
    RecommendedItem,
)
from app.services.ai import AIClient
from app.services.menu_items import MenuItemService


class RecommendationService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.ai = AIClient()
        self.menu_items = MenuItemService(session)
        self.recommendations = RecommendationRepository(session)

    async def recommend(self, user: User, payload: RecommendationRequest) -> RecommendationResponse:
        items: list[RecommendedItem] = []
        if payload.restaurant_id:
            menu_items = await self.menu_items.list_for_restaurant(user, payload.restaurant_id, limit=25)
            for item in menu_items[:5]:
                reason = "Matches availability and menu profile."
                if payload.preferences:
                    reason = f"Relevant to preferences: {', '.join(payload.preferences)}."
                items.append(RecommendedItem(name=item.name, reason=reason, score=0.8))

        if not items:
            items = [
                RecommendedItem(
                    name="Chef's balanced plate",
                    reason="A flexible default suggestion while menu data is being added.",
                    score=0.6,
                )
            ]

        model = "rules"
        summary = "FoodAI generated menu recommendations from available restaurant context."
        if payload.prompt:
            ai_summary = await self.ai.complete(
                "You are FoodAI, a concise restaurant recommendation assistant.",
                payload.prompt,
            )
            summary = ai_summary
            model = self.ai.model if self.ai.client else "rules"

        recommendation = Recommendation(
            user_id=user.id,
            restaurant_id=payload.restaurant_id,
            prompt=payload.prompt or "",
            response={
                "summary": summary,
                "items": [item.model_dump() for item in items],
                "model": model,
            },
            model=model,
        )
        await self.recommendations.add(recommendation)
        await self.session.commit()

        return RecommendationResponse(summary=summary, items=items, model=model)

    async def nutrition(self, payload: NutritionRequest) -> NutritionResponse:
        notes = await self.ai.complete(
            "Estimate nutrition conservatively and mention uncertainty.",
            f"Dish: {payload.dish_name}. Ingredients: {', '.join(payload.ingredients)}",
        )
        return NutritionResponse(
            dish_name=payload.dish_name,
            estimated_calories=None,
            notes=notes,
        )

    async def chat(self, payload: ChatRequest) -> ChatResponse:
        response = await self.ai.complete(
            "You are FoodAI, helping restaurant teams and guests with food choices.",
            payload.message,
        )
        return ChatResponse(response=response, model=self.ai.model if self.ai.client else "rules")
