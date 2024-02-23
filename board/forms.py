from django import forms
from .models import *


def postModelForm_for(model_class):
    class PostModelForm(forms.ModelForm):
        class Meta:
            model = model_class
            fields = ['title', 'body']
            labels = {
                'title': '제목',
                'body': '내용',
            }
    return PostModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'post', 'author']
