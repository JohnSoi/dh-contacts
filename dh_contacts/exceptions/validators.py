"""Модуль для исключений валидации"""

__author__: str = "Старков Е.П."

from dh_platform.exceptions import BaseAppException
from fastapi import status


class EmailIncorrect(BaseAppException):
    """Некорректный адрес электронной почты"""

    _DETAIL = "Введен не корректный адрес электронной почты"
    _CODE = status.HTTP_422_UNPROCESSABLE_ENTITY
