"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# myproject/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
import bots.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # websocket请求使用的路由
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns +
            bots.routing.websocket_urlpatterns
        )
    )
})