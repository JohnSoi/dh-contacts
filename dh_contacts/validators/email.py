"""Модуль для валидатора email"""

__author__: str = "Старков Е.П."

from email_validator import validate_email as lib_validate_email, EmailNotValidError

from dh_contacts.exceptions import EmailIncorrect


def validate_email(email: str) -> None:
    """
    Валидация email

    Args:
        email (str): Email для валидации
    Exceptions:
        EmailIncorrect - некорректный адрес Email
    """
    try:
        lib_validate_email(email, check_deliverability=False)
    except EmailNotValidError as exc:
        raise EmailIncorrect() from exc
