import os
from .websocket import routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        # 웹소켓 등록
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
        ),
    }
)


# WebSocket은 채팅을 위해 구현됨


# 서버생성 진입경로: asgi.py - routing.py - ChatConsumer.py

# asgi.py는 장고가 디렉토리 루트에서 기본 연결하여 진입함
# routing을 참고하여 경로와 ChatConsumer로 서버를 생성(as_asgi)하고 연결함
# ChatConsumer는 websocket의 연결을 관리하고 데이터를 처리함


# 클라이언트 진입경로: chat.js - ChatConsumer.py - chat.js

# chat.js에서 WebSocket에 연결함        new WebSocket - ChatConsumer.connect
# 입력창 텍스트를 서버로 전달           chatSocket.send
# 텍스트 처리해서 응답                  ChatConsumer.receive
# 클라이언트 메시지 수용                chatSocket.onmessage
