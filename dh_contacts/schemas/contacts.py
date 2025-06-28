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


class PrivateContactData(BaseModel):
    """
    Публичные данные КД

    Attributes:
        entity_id (int): Идентификатор связанной сущности
        entity_type (str): Тип связанной сущности
        value (str): Значение контакта
        contact_type (int): Тип контактных данных
        is_primary (bool): Основной контакт
    """

    entity_id: int
    entity_type: str
    value: str
    contact_type: int
    is_primary: bool