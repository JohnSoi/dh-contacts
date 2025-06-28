"""Модуль для сервиса"""

__author__: str = "Старков Е.П."

from dh_platform.services import BaseService

from .models import Contact as ContactModel


class ContactService(BaseService):
    """Сервис для работы с контактными данными"""

    _MODEL = ContactModel
