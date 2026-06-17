from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), default=None, index=True)
    restaurant_id: Mapped[UUID | None] = mapped_column(ForeignKey("restaurants.id", ondelete="SET NULL"), default=None, index=True)
    prompt: Mapped[str] = mapped_column(Text)
    response: Mapped[dict] = mapped_column(JSONB)
    model: Mapped[str] = mapped_column(String(120), default="rules")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User | None"] = relationship(back_populates="recommendations")
    restaurant: Mapped["Restaurant | None"] = relationship()
