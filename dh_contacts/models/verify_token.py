"""Модуль для модели токенов подтверждения контактных данных"""

__author__: str = "Старков Е.П."

from datetime import datetime

from dh_platform import models
from sqlalchemy import Boolean, DateTime, Enum, Integer, String, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from dh_contacts.consts import ContactType


class VerifyContactToken(models.BaseModel, models.IDMixin, models.UUIDMixin, models.TimestampMixin):
    contact_id: Mapped[int] = Column(Integer, ForeignKey("contact.id"))
    date_use: Mapped[datetime | None] = Column(DateTime)

    @property
    def is_used(self) -> bool:
        return self.date_use is not None
