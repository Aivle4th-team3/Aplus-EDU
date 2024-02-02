from django.urls import path, include
from allauth.account.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # 순서 주의. 앞선 path들이 뒤를 덮어씀
    # allauth 확장 path
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    # allauth 내장 path
    path('', include('allauth.urls')),
]
