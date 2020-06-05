from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default = timezone.now)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.task