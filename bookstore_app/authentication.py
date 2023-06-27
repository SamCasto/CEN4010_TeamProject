from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from bookstore_app import models

class CustomUserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        user = models.WebsiteUser.objects.filter(id=payload["id"]).first()

        return (user, None)