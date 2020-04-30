from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter

from sensor_app.consumers import SensorConsumer
from sensor_app.routing import websocket_urlpatterns
from django.urls import path

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
                [
                    path("ws/",SensorConsumer)
                ]
            )


})