from django.db import models

# Create your models here.


class UsersCrud(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField(max_length=20)
    profession = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    

   