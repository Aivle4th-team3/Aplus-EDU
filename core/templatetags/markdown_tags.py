from django import template
from django.conf import settings
from markdown import markdown
import os

register = template.Library()


@register.simple_tag
def load_markdown(filepath):
    try:
        for static_dir in settings.STATICFILES_DIRS:
            potential_path = os.path.join(static_dir, filepath)
            if os.path.exists(potential_path):
                with open(potential_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                return markdown(text)

    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."
    except Exception as e:
        return f"파일을 로드하는 중 오류가 발생했습니다: {e}"
