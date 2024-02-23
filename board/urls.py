from django.urls import path, include
from .models import *
from .views import *
from .forms import *
from django.views.generic import *


def urlpatterns_of(model):
    modelForm = postModelForm_for(model)
    return [
        path('', BoardListView.as_view(model=model), name='board'),
        path('<int:pk>/', BoardDetailView.as_view(model=model), name='detail'),

        path('new/', BoardCreateView.as_view(form_class=modelForm), name='create'),
        path('update/<int:pk>/', BoardUpdateView.as_view(model=model, form_class=modelForm), name='update'),
        path('delete/<int:pk>/', BoardDeleteView.as_view(model=model), name='delete'),
        path('<int:post_id>/create/comment/', CreateView.as_view(form_class=CommentForm), name='create_comment'),
        path('<int:post_id>/delete/comment/<int:pk>/', CommentDeleteView.as_view(model=Comment), name='delete_comment'),
    ]

urlpatterns = [
    path('', include((urlpatterns_of(Post), 'forum'), namespace='forum')),

    path('qna/', include((urlpatterns_of(QnA), 'qna'), namespace='qna')),

    path('community/', include((urlpatterns_of(Community), 'community'), namespace='community')),

    path('notice/', include((urlpatterns_of(Notice), 'notice'), namespace='notice')),
]
