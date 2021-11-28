from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=254)
    username=None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return  str(self.name)