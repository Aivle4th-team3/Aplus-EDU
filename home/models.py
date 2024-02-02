from django.db import models
from accounts.models import User


class Calendar(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    label = models.CharField(max_length=250)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
