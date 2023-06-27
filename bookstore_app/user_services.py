import dataclasses
from typing import TYPE_CHECKING
from bookstore_app import models
import datetime
import jwt
from django.conf import settings

if TYPE_CHECKING:
    from .models import WebsiteUser

@dataclasses.dataclass
class UserDataClass:
    first_name: str
    last_name: str
    email: str
    username: str
    address: str = None
    credit_card_number: str = None
    password: str = None
    id: int = None

    @classmethod
    def from_instance(cls, user: "WebsiteUser") -> "UserDataClass":
        return cls(
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            username = user.username,
            id = user.id,
        )


def create_user(user_dc: "UserDataClass") -> "WebsiteUser":
    instance = models.WebsiteUser(
        first_name = user_dc.first_name,
        last_name = user_dc.last_name,
        email = user_dc.email,
        username = user_dc.username,
        address=user_dc.address,
        credit_card_number = user_dc.credit_card_number
    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return UserDataClass.from_instance(instance)


def user_username_selector(username:str) -> "WebsiteUser":
    user = models.WebsiteUser.objects.filter(username=username).first()

    return user

def create_token(user_id:int) -> str:
    payload = dict(
        id = user_id,
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat = datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token