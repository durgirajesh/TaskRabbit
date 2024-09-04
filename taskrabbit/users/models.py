from django.db import models
from django.contrib.auth.models import User

class UserTasks(models.Model) :
    task_name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_description = models.TextField(max_length=100)
    