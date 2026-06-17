from openai import AsyncOpenAI

from app.core.config import settings


class AIClient:
    def __init__(self) -> None:
        self.model = settings.OPENAI_MODEL
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None

    async def complete(self, system_prompt: str, user_prompt: str) -> str:
        if self.client is None:
            return "AI provider is not configured. Using rule-based FoodAI suggestions."

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
        )
        return response.choices[0].message.content or "No recommendation generated."
