from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'user_message', 'bot_message')


admin.site.register(Message, MessageAdmin)
