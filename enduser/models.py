from typing import ContextManager
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class note(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title+str(self.user_id)

class todo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

