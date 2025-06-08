"""Модуль для схем данных при регистрации"""

__author__: str = "Старков Е.П."

from pydantic import BaseModel


class UserRegisterContactField(BaseModel):
    """
    Поля при регистрации пользователя

    Attributes:
        email (str): Email пользователя
    """

    email: str
