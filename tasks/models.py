from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  #optional field
    date = models.DateField(default=timezone.now)  #Added the date field
    completed = models.BooleanField(default=False, blank=True, null=True) #Like a Checklist 

    def __str__(self):
        return self.title
