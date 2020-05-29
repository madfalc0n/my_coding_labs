from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} / {self.age} / {self.weight} / {self.height}"