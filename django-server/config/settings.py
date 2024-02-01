"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

### Happy New Year~~~! ###

import os
import environ
from pathlib import Path
from student_ai import Chatbot

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 장고 ASGI(Asynchronous Server Gateway Interface) 프로토콜 지원 웹서버
    # 웹소켓에 필요
    'daphne',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 장고 OAuth 계정 관리
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.github',
    # DB용 필드
    'phonenumber_field',
    'django_countries',
    # 외부 저장소 연결 Google Cloud Storage, AWS S3 등
    'storages',
    # 게시글 에디터
    'ckeditor',
    'ckeditor_uploader',

    # 사용자 앱 페이지
    'accounts',
    'home',
    'lecture',
    'chat',
    'board',
    'evaluation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'config.message.MessageMiddleware',
]


# WSGI: Web Server Gateway Interface
# Python에서 웹 서버 호스팅 하기 위한 인터페이스
WSGI_APPLICATION = 'config.wsgi.application'

# ASGI: Asynchronous Server Gateway Interface
# WSGI의 비동기 확장 버전, 웹소켓에 사용
# 실시간 기능에 필요 (채팅 기능에 사용함)
ASGI_APPLICATION = "chat.asgi.application"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTHENTICATION_CLASSES = (
    # ...
    'allauth.socialaccount.providers.oauth2.client.OAuth2',
    # ...
)


AUTH_USER_MODEL = 'accounts.User'

# 소셜 로그인 관련 설정
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': env('GOOGLE_OAUTH_CLIENT_ID'),
            'secret': env('GOOGLE_OAUTH_SECRET'),
            'key': ''
        }
    },
    'naver': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': env('NAVER_OAUTH_CLIENT_ID'),
            'secret': env('NAVER_OAUTH_SECRET'),
            'key': ''
        }
    },
    'kakao': {
        'SCOPE': ['profile_nickname', 'profile_image'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': env('KAKAO_OAUTH_CLIENT_ID'),
            'secret': env('KAKAO_OAUTH_SECRET'),
        }
    },
    'github': {
        'METHOD': 'oauth2',
        'SCOPE': ['user:email'],
        'APP': {
            'client_id': env('GITHUB_OAUTH_CLIENT_ID'),
            'secret': env('GITHUB_OAUTH_SECRET'),
        }
    }
}

# allauth site_id
SITE_ID = 1

# 회원 가입 ID 타입
ACCOUNT_AUTHENTICATION_METHOD = 'username'  # or email, userusername_email
# 로그인 후 리디렉션할 페이지
LOGIN_REDIRECT_URL = 'home'
# 가입 후 리디렉션할 페이지
ACCOUNT_SIGNUP_REDIRECT_URL = 'frontdoor'
# 로그아웃 후 리디렉션할 페이지
ACCOUNT_LOGOUT_REDIRECT_URL = 'frontdoor'
# 로그아웃 버튼 클릭 시 자동 로그아웃
ACCOUNT_LOGOUT_ON_GET = True
# 브라우저 닫을 때 세션 쿠키 유지할지
ACCOUNT_SESSION_REMEMBER = False

# 소셜 계정으로 로그인 시 자동으로 사용자 계정을 생성할지
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_FORMS = {
    # 소셜계정 가입 후 추가 폼
    'signup': 'accounts.forms.CustomSocialSignupForm',
}

# URL 진입점
ROOT_URLCONF = 'config.urls'

# 템플릿(html) 경로 설정
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context.context_processor',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aivledb',
        'USER': env('DB_MASTER_USER_ID'),
        'PASSWORD': env('DB_MASTER_USER_PWD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
    if env('ENVIRONMENT') == "PRODUCTION" else
    {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # 데이터베이스 파일 경로
    }
}

# 외부 저장소 Amazon S3
if env('ENVIRONMENT') == "PRODUCTION":
    # AWS Setting
    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = 'ktaivle-team3-bucket'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
        AWS_STORAGE_BUCKET_NAME, AWS_REGION)

    # Media Setting
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 미디어 파일 기본 저장소
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 게시글 에디터 설정
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms', 'items': ['Form', 'Checkbox', 'Radio', 'TextField',
                                        'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField']},
            '/',  # put this to force next toolbar on new line
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': [
                'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            {'name': 'yourcustomtools', 'items': ['Preview', 'Maximize']},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', 'div', 'autolink', 'autoembed', 'embedsemantic', 'autogrow',
            # 'devtools',
            'widget', 'lineutils', 'clipboard', 'dialog', 'dialogui', 'elementspath'
        ]),
    }
}

# AI 패키지 사용
chatbot = Chatbot(
    llm_provider=env('AI_PROVIDER'),
    llm_model=env(env('AI_PROVIDER')+'_AI_MODEL'),
    llm_api_key=env(env('AI_PROVIDER')+'_API_KEY'),
    
    embedding_provider=env('EMBEDDING_PROVIDER'),
    embedding_model=env(env('EMBEDDING_PROVIDER')+'_EMBEDDING_MODEL'),
    embedding_api_key=env(env('EMBEDDING_PROVIDER')+'_API_KEY'),
    vectorstore_provider=env('VECTORSTORE_PROVIDER'),
    is_test=False)
