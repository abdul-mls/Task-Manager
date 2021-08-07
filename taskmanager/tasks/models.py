from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.

class Importance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    importance = models.ForeignKey(Importance, null=True, blank=False, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    ending_date = models.DateTimeField(null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ending_date']
