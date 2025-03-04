from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/ticket/', TicketConsumer.as_asgi())
]