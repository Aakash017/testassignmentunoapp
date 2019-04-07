from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True,max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_verified =models.BooleanField(default=False)

    def __str__(self):
        return self.email

class UserConfirmation(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    token = models.CharField(max_length=255)



