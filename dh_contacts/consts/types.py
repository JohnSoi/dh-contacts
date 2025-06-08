"""Пакет для типов контактных данных"""

__author__: str = "Старков Е.П."
from enum import IntEnum

HUMAN_TYPE_NAME: dict[str, str] = {
    "PHONE": "Телефон",
    "EMAIL": "Email",
    "TELEGRAM": "Telegram",
    "WHATSAPP": "WhatsApp",
    "VK": "ВК",
    "SITE": "Сайт",
    "OTHER": "Другое",
}


class ContactType(IntEnum):
    """Типы контактных данных пользователя"""

    PHONE = 1  # Телефон
    EMAIL = 2  # Электронная почта
    TELEGRAM = 3  # Telegram
    WHATSAPP = 4  # WhatsApp
    VK = 5  # ВКонтакте
    SITE = 6  # Сайт
    OTHER = 99  # Другой тип контакта

    @classmethod
    def choices(cls):
        """Варианты для выбора в формате для БД"""
        return [(key.value, HUMAN_TYPE_NAME.get(key.name)) for key in cls]
