from django.contrib import admin
from .models import TestPaper


class TestPaperAdmin(admin.ModelAdmin):
    list_display = ('question', 'video')


admin.site.register(TestPaper, TestPaperAdmin)
