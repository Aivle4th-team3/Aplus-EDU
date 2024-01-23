from django.urls import path
from allauth.account.views import PasswordResetView
from . import views

# app_name: URL 네임스페이스 사용
# 템플릿에서 참조할 수 있음
app_name = "accounts"

urlpatterns = [
    path('password/reset/', PasswordResetView.as_view(), name='reset_password'),
    path('mypage/', views.mypage, name='mypage'),
    path('consent/', views.consent, name='consent'),
    path('delete/', views.delete, name='delete'),
    path('readmessage/', views.read_message, name='readmessage'),
]
