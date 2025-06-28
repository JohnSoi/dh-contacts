"""Модуль для исключений"""

__author__: str = "Старков Е.П."

from dh_platform.exceptions import BaseAppException
from fastapi import status


class EmailAlreadyExists(BaseAppException):
    """Некорректный адрес электронной почты"""

    _DETAIL = "Введенный адрес электронной почты уже используется"
    _CODE = status.HTTP_409_CONFLICT
