from datetime import date
from datetime import timedelta
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserRegistrationBody(BaseModel):
    username: str = Field(..., examples=["Elon"])
    password: str = Field(..., examples=["qwerty"])
    email: EmailStr = Field(..., examples=["elon@gmail.com"])
    date_of_birth: date = Field(..., examples=[date.today()])


class UserLoginBody(BaseModel):
    email: EmailStr = Field(..., examples=["Elon"])
    password: str = Field(..., examples=["qwerty"])
