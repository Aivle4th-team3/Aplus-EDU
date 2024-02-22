from django.urls import path, include
from . import views
from .models import *


forum_view = views.Which(Post, 'forum')
qna_view = views.Which(QnA, 'qna')
community_view = views.Which(Community, 'community')
notice_view = views.Which(Notice, 'notice')

def urlpatterns_of(view):
    return [
        path('', view.board, name='board'),
        path('<int:no>/', view.detail, name='detail'),

        path('new/', view.post_create, name='create'),
        path('update/<id>/', view.post_update, name='update'),
        path('delete/<id>/', view.post_delete, name='delete'),
        path('<int:id>/create/comment/', view.create_comment, name='create_comment'),
        path('<int:id>/delete/comment/<int:comment_id>/', view.delete_comment, name='delete_comment'),
    ]

urlpatterns = [
    path('', include((urlpatterns_of(forum_view), 'forum'), namespace='forum')),

    path('qna/', include((urlpatterns_of(qna_view), 'qna'), namespace='qna')),

    path('community/', include((urlpatterns_of(community_view), 'community'), namespace='community')),

    path('notice/', include((urlpatterns_of(notice_view), 'notice'), namespace='notice')),
]
