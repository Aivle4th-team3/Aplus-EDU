from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from lecture.models import Video
from accounts.models import User
from chat.models import Message
from config.settings import chatbot
from chat.services.tts import tts
import urllib.parse
import json

# Consumer: 메시지를 받아서 작업 수행


class ChatConsumer(WebsocketConsumer):
    # 연결 관리
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    # 데이터 처리
    def receive(self, text_data):
        # 쿼리 문자열 파싱 /?key=value
        query_string = self.scope['query_string'].decode('utf8')
        params = urllib.parse.parse_qs(query_string)
        # 쿼리 파라미터 추출
        video_id = params.get('video_id', [None])[0]
        # 채팅방 파라미터 추출
        user_id = self.scope['url_route']['kwargs']['room_name']
        # DB 참조 객체
        video = Video.objects.get(id=video_id)
        user = User.objects.get(id=user_id)
        # video-user 쌍의 테이블명
        tablename = f"{video_id}-{user_id}"

        # 입력 받은 질문
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_time = datetime.now()

        # 검색할 테이블명과 현재 메시지를 전송
        # chatbot은 데이터베이스를 가지고 이전 메시지들을 기억
        # 챗봇 응답
        bot_message = chatbot.chat(tablename, message)
        answer_time = datetime.now()

        print("query", message)
        print("answer", bot_message)

        # 답변을 tts로 변환
        audio_message = tts(bot_message)

        # Message 생성
        instance = Message(
            user=user, video=video,
            user_message=message, bot_message=bot_message,
            user_time=message_time, bot_time=answer_time)
        # 데이터베이스에 저장
        instance.save()
        self.send(text_data=json.dumps(
            {"message": bot_message, "audioMessage": audio_message}))
