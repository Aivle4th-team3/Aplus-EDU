from django import forms
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django_countries import countries
from .models import User


# Form: HTML 입력 폼
# 기본 가입 폼 추가
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # 필드에 새로운 라벨링
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'
        self.fields['avatar'].label = '프로필 이미지'

        # 필드들 꺼내서 속성에 값 추가
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


# 소셜로그인 후 가입 폼 추가
class CustomSocialSignupForm(SocialSignupForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomSocialSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'
        self.fields['avatar'].label = '프로필 이미지'

        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        return user


# ModelForm: model(User)로부터 필드정보를 읽어 자동으로 폼 필드 설정
class UserForm(forms.ModelForm):

    country = forms.ChoiceField(
        choices=countries, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        # 추가 설정 해주려고 따로 그룹화
        fields = ['first_name', 'last_name', 'email',
                  'country', 'phone_number', 'avatar']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '010 0000 0000'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'
        self.fields['avatar'].label = '프로필 이미지'
        self.fields['country'].label = '국가'
        self.fields['phone_number'].label = '전화번호'

        for field in self.fields:
            # 리스트 목록의 필드들은 필수가 아님
            self.fields[field].required = False
