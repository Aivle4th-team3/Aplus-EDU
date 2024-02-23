from .forms import CommentForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from math import ceil
from typing import Any
from django.http.request import HttpRequest
from django.urls import reverse

# 전체 목록 보기
class BoardListView(ListView):
    template_name = 'board/post_list.html'

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)
        # 날짜순 기본 정렬
        self.queryset = self.model.objects.order_by('-created')

    def get_queryset(self):
        # 검색 쿼리 들어올시 필터링
        self.search_key = self.request.GET.get('q', '')
        queryset = super().get_queryset()

        return queryset.filter(title__contains=self.search_key)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # pagination
        namespace = self.request.resolver_match.namespace
        page = int(self.request.GET.get('page', 1))
        per = int(self.request.GET.get('per', 10))
        total = len(self.object_list)
        last = ceil(total/per)
        board_list = range(1, last+1)
        per_list = [7, 10, 20, 50]
        start = per*(page-1)
        end = per*page

        context.update({
            'namespace': namespace,
            'post_all': self.object_list[start:end], 'q': self.search_key, 'page': page, 'per': per,
            'board_list': board_list, 'per_list': per_list, 'total': total, 'last': last
        })
        return context

# 상세 보기
class BoardDetailView(DetailView):
    template_name = 'board/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        namespace = self.request.resolver_match.namespace
        comment_list = self.object.comments.all()
        tag_list = self.object.tag.all()

        comment_form = CommentForm()
        context.update({
            'namespace': namespace,
            'comment_all': comment_list, 'tag_list': tag_list, 'comment_form': comment_form
        })

        return context

class BoardCreateView(CreateView):
    template_name = 'board/post_form.html'

    def form_valid(self, form):
        # 폼 인스턴스를 저장하기 전 처리
        form.instance.author = self.request.user
        # 저장
        return super().form_valid(form)

class BoardUpdateView(UpdateView):
    template_name = 'board/post_form.html'

class BoardDeleteView(DeleteView):
    template_name = 'board/confirm_delete.html'

    def get_success_url(self):
        return reverse(f"{self.request.resolver_match.namespace}:board")

class CommentDeleteView(DeleteView):
    template_name = 'board/confirm_delete.html'

    def get_success_url(self):
        return reverse(f"{self.request.resolver_match.namespace}:detail", args=[self.kwargs['post_id']])
