from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RecommendationRequest(BaseModel):
    restaurant_id: UUID | None = None
    preferences: list[str] = []
    dietary_restrictions: list[str] = []
    budget: float | None = None
    prompt: str | None = None


class RecommendedItem(BaseModel):
    name: str
    reason: str
    score: float


class RecommendationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    summary: str
    items: list[RecommendedItem]
    model: str


class NutritionRequest(BaseModel):
    dish_name: str
    ingredients: list[str] = []


class NutritionResponse(BaseModel):
    dish_name: str
    estimated_calories: int | None
    notes: str


class ChatRequest(BaseModel):
    message: str
    restaurant_id: UUID | None = None


class ChatResponse(BaseModel):
    response: str
    model: str
