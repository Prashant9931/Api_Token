from django.db import models
from django.contrib.auth.models import User,auth
class Book(models.Model):
    id = models.IntegerField(primary_key= True)
    title = models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
