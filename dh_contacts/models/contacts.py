"""Модуль для модели контактов"""

__author__: str = "Старков Е.П."

from dh_platform import models
from sqlalchemy import Boolean, DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from dh_contacts.consts import ContactType


class Contact(models.BaseModel, models.IDMixin, models.UUIDMixin, models.TimestampMixin, models.SoftDeleteMixin):
    """Модель для хранения контактных данных пользователя"""

    entity_id: Mapped[int] = mapped_column(Integer, nullable=False)
    entity_type: Mapped[str] = mapped_column(String(20), nullable=False)
    contact_type: Mapped[ContactType] = mapped_column(Enum(ContactType), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    date_verify = mapped_column(DateTime, nullable=True)
    is_primary = mapped_column(Boolean, default=False)

    @property
    def is_verify(self) -> bool:
        """Контакт подтвержден"""
        return self.date_verify is not None

    def __repr__(self):
        return f"<UserContact {self.contact_type.name}:{self.value}>"
