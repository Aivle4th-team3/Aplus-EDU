from django.db import models
from pgvector.django import VectorField
from accounts.models import User
from lecture.models import Video
from student_ai import Exchange

# Create your models here.


class Message(models.Model):
    # enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=False, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=False)

    user_time = models.DateTimeField(null=True)
    bot_time = models.DateTimeField(null=True)

    user_message = models.TextField()
    bot_message = models.TextField()
    user_message_embedded = VectorField(dimensions=1536)
    bot_message_embedded = VectorField(dimensions=1536)

    def to_exchange(self):
        return Exchange(self.user_message, self.user_message_embedded, self.bot_message, self.bot_message_embedded)
