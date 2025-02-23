from django.urls import path
from hospital_app.consumers import MyConsumer

websocket_urlpatterns = [
    path("ws/some_path/", MyConsumer.as_asgi()),
]
