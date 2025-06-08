"""Модуль для схем данных контактов"""

__author__: str = "Старков Е.П."

from pydantic import BaseModel

from dh_contacts.consts import ContactType


class PublicContactData(BaseModel):
    """
    Публичные данные КД

    Attributes:
        type (ContactType): Тип контакта
        value (str): Значение контакта
        is_verify (bool): Контакт подтвержден
    """

    type: ContactType
    value: str
    is_verify: bool
