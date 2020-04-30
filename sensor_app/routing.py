from django.urls import re_path
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('sensors/all/$', consumers.SensorConsumer),
]