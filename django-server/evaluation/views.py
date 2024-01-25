import json
from itertools import groupby
from django.shortcuts import render
from .models import TestResult
import asyncio
from config.settings import chatbot
from accounts.models import User
from lecture.models import Video
from chat.models import Message
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.clickjacking import xframe_options_exempt

# 쓰레딩
async def __threading(memory, statements):
    # 결과 저장할 가변 리스트
    # question, answer, test_paper, evaluation
    eval_results = [['', '', '', ''] for _ in range(len(statements))]

    threads = []
    for eval_result, statement in zip(eval_results, statements):
        question = statement.question
        answer = statement.answer
        test = chatbot.test(memory)  # 질문에 답하는 테스트 함수

        thread = asyncio.to_thread(chatbot.eval_test, question, answer, test, eval_result)
        threads.append(thread)

    # 각각 쓰레드 수행
    await asyncio.gather(*threads)

    # 결과
    explanations = []
    scores = []
    test_papers = []
    for er in eval_results:
        print(*map(': '.join, zip(["문제", "답", "풀이", "점수 및 보완할 부분"], er)), sep='\n')
        idx = er[3].find(':')
        if idx!=-1:
            point, explain = er[3][:idx], er[3][idx+1:]
        else:
            point, explain = 0, "응답 오류"
        explanations.append(explain)
        test_papers.append(er[2])
        point = int(point)
        scores.append(point)

    return scores, explanations, test_papers

@xframe_options_exempt
def evaluation(request, lecture_name, video_name):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
        video_id = request.POST['video_id']
        video = Video.objects.get(id=video_id)

        # 과거 채팅 메시지들
        memory = Message.objects.filter(user=user_id, video=video_id)

        # 문제지 & 정답지
        statements = Video.objects.get(id=video_id).testpapers.all()

        # 쓰레딩 처리
        scores, explanations, test_papers = asyncio.run(__threading(memory, [*statements]))
        # statements는 장고 ORM 객체
        # 비동기 작업에서 동기적인 장고 ORM 쿼리를 실행하면 오류가 생김. 그래서 풀어준다.

        # 결과 정리
        mean_score = sum(scores)/(len(scores) if len(scores) else 1)
        correct_count = sum(1 for score in scores if score >= 70)
        wrong_count = len(scores) - correct_count

        # TestResult 종합 점수로 데이터베이스에 저장
        instance = TestResult(user=user, video=video, score=mean_score)
        instance.save()

        # 이번 평가의 점수와 설명
        evals = [{'score': score,
                  'explation': explation,
                  'student_saying': test_paper,
                  } for score, explation, test_paper in zip(scores, explanations, test_papers)]

        # 유저당 점수의 기록
        test_results = TestResult.objects.filter(user=user, video=video)
        fields_data = [{'evaluation_date': obj.evaluation_date,
                        'score': obj.score} for obj in test_results]
        json_result = json.dumps(fields_data, cls=DjangoJSONEncoder)

        context = {
            'score': mean_score,
            'lecture_name': lecture_name,
            'video_name': video_name,
            'num_correct': correct_count,
            'num_wrong': wrong_count,
            'detail_evals': evals,
            'history_evals': json_result,
        }
    else:
        context = {
            'lecture_name': lecture_name,
        }
    return render(request, "./evaluation/page.html", context=context)


def my_evaluation(request):
    user = request.user

    # 유저의 테스트 결과를 그룹화
    instances = TestResult.objects.filter(user=user).order_by('video_id')
    groups = {k: list(g) for k, g in groupby(instances, lambda x: x.video_id)}
    grouped_scores = {
        Video.objects.get(id=k).name: [instance.score for instance in g]
        for k, g in groups.items()}

    context = {
        'grouped_scores': grouped_scores,
    }
    return render(request, "./evaluation/my.html", context=context)
