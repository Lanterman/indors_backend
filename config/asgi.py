import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .middlewares import TokenAuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from apps.main import routings as main_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        TokenAuthMiddlewareStack(
            URLRouter(
                main_routing.websocket_urlpatterns,
            )
        )
    )
})
