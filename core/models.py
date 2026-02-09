from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class taskdata(models.Model):
    priority_choice =[
        (1,"HIGH"),
        (2,"MEDIUM"),
        (3,"LOW"),
    ]
    priority = models.IntegerField(choices=priority_choice,default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
