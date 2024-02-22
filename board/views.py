from django.shortcuts import render, get_object_or_404, redirect
from math import ceil
from .models import *
from .forms import *


# forum, community, notice, qna - View를 생성하는 클래스
# View의 구현은 동일한걸 사용한다.
# 인스턴스를 구분하기 위해 Model, namespace를 인수로 받는다.
class Which:
    def __init__(self, Model, namespace):
        self.Model = Model
        self.namespace = namespace

    # 전체 목록 보기
    def board(self, request):
        search_key = request.GET.get('q', '')
        post_list = self.Model.objects.filter(title__contains=search_key)
        post_list = post_list.order_by('-id')
        for post in post_list:
            post.category = post.__class__.__name__

        page = int(request.GET.get('page', 1))
        per = int(request.GET.get('per', 10))
        total = len(post_list)
        last = ceil(total/per)
        board_list = range(1, last+1)
        per_list = [7, 10, 20, 50]

        start = per*(page-1)
        end = per*page

        return render(request, 'board/board.html', {
            'namespace': self.namespace,
            'post_all': post_list[start:end], 'q': search_key, 'page': page, 'per': per,
            'board_list': board_list, 'per_list': per_list, 'total': total, 'last': last})

    # 상세 보기
    def detail(self, request, no):
        post = get_object_or_404(self.Model, id=no)  # 인스턴스
        comment_list = post.comments.all()  # QuerySet
        tag_list = post.tag.all()  # QuerySet

        comment_form = CommentForm()
        return render(request, 'board/detail.html', {
            'namespace': self.namespace,
            'post': post, 'comment_all': comment_list, 'tag_list': tag_list, 'comment_form': comment_form})

    def post_create(self, request):
        # 설정된 모델에 맞게 모델폼의 인스턴스를 만들고 POST 받아온 데이터를 추가한다.
        form = PostModelForm(request.POST or None, instance=self.Model())
        if form.is_valid():
            # DB에 추가
            # 모델 인스턴스만 만들어지고 저장은 안 됨: commit=False
            post = form.save(commit=False)
            post.author = request.user
            post.namespace = self.namespace
            post.save()
            # get_absolute_url이 POST에서 자동으로 실행: return은 HttpResponse
            return redirect(post)

        return render(request, 'board/post.html', {'form': form})

    # Form 기반 Data 수정
    def post_update(self, request, id):
        # 수정해야할 모델을 불러온다
        post = get_object_or_404(self.Model, id=id)
        # 불러온 모델로 모델폼의 인스턴스를 만들고 POST 받아온 데이터를 추가한다.
        form = PostModelForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()  # 추가도 하고 수정도 가능, 구분은 새로운 데이터면 추가 디비에서 가져온거면 수정
            return redirect(f'{self.namespace}:detail', id)

        return render(request, 'board/post.html', {'form': form})

    # Data 삭제 작업
    def post_delete(self, request, id):
        post = get_object_or_404(self.Model, id=id)
        post.delete()
        return redirect(f'{self.namespace}:board')
    
    def create_comment(self, request, id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = get_object_or_404(self.Model, id=id)
                comment.author = request.user
                comment.save()
                return redirect(f'{self.namespace}:detail', id)

    def delete_comment(self, request, id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect(f'{self.namespace}:detail', id)
