from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class notes_create(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    note=models.CharField(max_length=500)
    created=models.DateField(auto_now_add=True)
