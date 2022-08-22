from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    start_date = models.DateField(default=timezone.now)
    finished_date = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="todo_user")
    token = models.ForeignKey(Token, on_delete=models.CASCADE, related_name="todo_token",null=True, blank=True)
    is_active = models.BooleanField(default = True)
    is_completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title

