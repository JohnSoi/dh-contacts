from dh_platform.patterns.message_bus import message_bus
from dh_users.schemas.events import UserValidateEvent, UserAddEvent, UserDeleteEvent

from dh_contacts.consts import ContactType
from dh_contacts.exceptions import EmailIncorrect, EmailAlreadyExists
from dh_contacts.schemas import PrivateContactData
from dh_contacts.services import ContactService
from dh_contacts.validators import validate_email
from dh_contacts.models import Contact as ContactModel


async def _validate_email(data: UserValidateEvent) -> None:
    email: str | None = data.email

    if not email or validate_email(email):
        raise EmailIncorrect()

    if await ContactService.get_one_by_filter(value=email, contact_type=ContactType.EMAIL):
        raise EmailAlreadyExists()


async def _create_contact_data(data: UserAddEvent) -> None:
    await ContactService.create(PrivateContactData(**{
        "entity_id": data.user_id,
        "entity_type": "user",
        "value": data.email,
        "contact_type": ContactType.EMAIL,
        "is_primary": True,
    }))


async def _delete_contact_data(data: UserDeleteEvent) -> None:
    contacts: list[ContactModel] = await ContactService.list(
        {"entity_id": data.user_id, "entity_type": "user"}
    )

    for contact in contacts:
        await ContactService.delete(contact.id)


def contacts_event_subscribe() -> None:
    message_bus.subscribe(UserValidateEvent, _validate_email)
    message_bus.subscribe(UserAddEvent, _create_contact_data)
    message_bus.subscribe(UserDeleteEvent, _delete_contact_data)