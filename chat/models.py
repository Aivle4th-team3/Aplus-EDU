from django.db import models
from accounts.models import User
from lecture.models import Video


class Conversation(models.Model):
    """
    - N:1 relationship with User
    - N:1 relationship with Video
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'video'),
                name='user-video composite key'
            ),
        ]

    def __str__(self):
        return f'{self.user}/{self.video}'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=False)


class Message(models.Model):
    """
    - N:1 relationship with Conversation
    """
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=False, related_name='messages')

    user_time = models.DateTimeField(null=True)
    bot_time = models.DateTimeField(null=True)

    user_message = models.TextField()
    bot_message = models.TextField()
