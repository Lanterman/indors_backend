from django.urls import path, include
from rest_framework import permissions
from rest_framework.settings import api_settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings
from apps.user.auth.backends import JWTTokenAuthBackend


AUTH_HEADER_TYPES = settings.JWT_SETTINGS["AUTH_HEADER_TYPES"]

contact = openapi.Contact(name="Lanterman", url="https://github.com/Lanterman", email='klivchinskydmitry@gmail.com')

schema_url_patterns = [
   path("api/v1/", include('apps.urls')),
]

description = f"""
For authenticated requests, create a user and enter the resulting token along with the word '{AUTH_HEADER_TYPES}'.
Example: '{AUTH_HEADER_TYPES} d8175af2fac77d4ee16b984769a7251775e6be48'.


P.S.
To test the functionality of the "Celery Task" and "/auth/profile/try_to_reset_password/" endpoint, you need to set the following environment variables:
1. '.env' file:
   1.1. EMAIL_HOST_USER
   1.2. EMAIL_HOST_PASSWORD
2. '.env.dev' file:
   1.1. DOC_EMAIL_HOST_USER
   1.2. DOC_EMAIL_HOST_PASSWORD

P.S.S.
Before resetting "auth/reset_password/<email>/<secret_key>/" password, you must request it from "/auth/profile/try_to_reset_password/" endpoint.
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Indors Navigation test",
      default_version=api_settings.DEFAULT_VERSION,
      description=description,
      license=openapi.License(name="BSD License"),
      contact=contact,
   ),
   public=True,
   patterns=schema_url_patterns,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[JWTTokenAuthBackend]
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
