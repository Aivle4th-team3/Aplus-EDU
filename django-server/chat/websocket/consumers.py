from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from lecture.models import Video
from accounts.models import User
from chat.models import Message
from chat.services.talk_to_bot import talk_to_bot
from chat.services.tts import tts
import urllib.parse
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # 쿼리 문자열 파싱 /?key=value
        query_string = self.scope['query_string'].decode('utf8')
        params = urllib.parse.parse_qs(query_string)
        # 쿼리 파라미터 추출
        video_id = params.get('video_id', [None])[0]
        # 방 파라미터 추출
        user_id = self.scope['url_route']['kwargs']['room_name']

        # 참조 객체들
        video = Video.objects.get(id=video_id)
        user = User.objects.get(id=user_id)
        # 이전 메시지들
        user_messages = Message.objects.filter(user=user, video=video)


        # 입력 받은 질문
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_time = datetime.now()

        # 챗봇 응답
        answer, user_message_embedded, bot_message_embedded = talk_to_bot(message, user_messages)
        answer_time = datetime.now()

        print("query", message)
        print("answer", answer)


        # gpt 답변 tts로 변환
        audio_message = tts(answer)

        # Message 생성
        instance = Message(
            user=user, video=video,
            user_message=message, bot_message=answer, user_time=message_time, bot_time=answer_time,
            user_message_embedded=user_message_embedded, bot_message_embedded=bot_message_embedded)
        # 데이터베이스에 저장
        instance.save()

        self.send(text_data=json.dumps({"message": answer, "audioMessage": audio_message}))
