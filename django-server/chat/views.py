import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.http import require_http_methods
from .models import Message
from accounts.models import User
from lecture.models import Video
from .services.stt import stt


@xframe_options_exempt
def chat(request, lecture_name, video_name):
    # user, video id를 POST로 전송 받음
    user_id = request.POST['user_id'] if request.method == 'POST' else None
    video_id = request.POST['video_id'] if request.method == 'POST' else None
    user = User.objects.get(id=user_id)
    video = Video.objects.get(id=video_id)

    # 메시지검색
    messages = Message.objects.filter(user=user, video=video)

    # 기록 읽기
    history = [[{'type': 'user', 'message': message.user_message, 'time': message.user_time},
                {'type': 'bot',  'message': message.bot_message,  'time': message.bot_time}] for message in messages]

    context = {
        'lecture_name': lecture_name,
        'video': video,
        'user': user,
        'history': history,
    }
    return render(request, "./chat/page.html", context)


# 전송된 음성을 STT로 바꿔서 응답
@require_http_methods(["POST"])
def voice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        base64AudioMessage = data['message']

        text = stt(base64AudioMessage)

        return JsonResponse({'status': 'success', 'text': text})
