from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # ChatConsumer에서 인스턴스 생성해서 경로와 연결
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]
