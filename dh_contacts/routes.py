"""Модуль для роутов"""

__author__: str = "Старков Е.П."

from uuid import UUID

from dh_contacts.schemas import ConfirmData
from dh_contacts.services import ContactService
from fastapi import APIRouter

contact_routes: APIRouter = APIRouter(prefix="/contacts", tags=["contacts"])


@contact_routes.get(
    "/confirm/{token}", description="Подтверждение контакта по токену",
)
async def contact_confirm(token: UUID) -> bool:
    """Подтверждение котнтакта по токену"""
    return await ContactService.confirm(token)


@contact_routes.post(
    "/confirm/send", description="Отправка письма подтверждения на почту"
)
async def contact_confirm_send(contact_data: ConfirmData) -> bool:
    return await ContactService.send_confirm_email(contact_data.email)
