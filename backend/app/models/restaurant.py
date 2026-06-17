from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    name: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    address: Mapped[str | None] = mapped_column(String(500), default=None)
    phone: Mapped[str | None] = mapped_column(String(50), default=None)
    cuisine_type: Mapped[str | None] = mapped_column(String(120), default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    owner: Mapped["User"] = relationship(back_populates="restaurants")
    categories: Mapped[list["Category"]] = relationship(
        back_populates="restaurant",
        cascade="all, delete-orphan",
    )
    menu_items: Mapped[list["MenuItem"]] = relationship(
        back_populates="restaurant",
        cascade="all, delete-orphan",
    )
    orders: Mapped[list["Order"]] = relationship(
        back_populates="restaurant",
        cascade="all, delete-orphan",
    )
