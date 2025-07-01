from pydantic import BaseModel, EmailStr


class ConfirmData(BaseModel):
    email: EmailStr
