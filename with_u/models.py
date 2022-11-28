from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.models import UserManager

class Categorie(models.Model):
    title = models.CharField(max_length = 50)
    language = models.CharField(max_length = 50)
    type = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.title

class Member(AbstractUser):
    name = models.CharField(max_length = 50,unique=True)
    address = models.CharField(max_length = 50)
    phone_number =  models.CharField(max_length = 12)
   

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    
    """
    user directory path

    """
    return 'user_{0}/{1}'.format(instance.member.id, filename)

class Datacollection(models.Model):
    user = models.ForeignKey(Member,on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    link = models.URLField()
    text = models.TextField(max_length=200)

class Relatives(models.Model):
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    withucommunity = models.CharFiled(max_length=1)

class Bot(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='member')
    collection = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    data = models.ForeignObjectRel(Datacollection, on_delete=models.CASCADE)
    contacts = models.ManyToManyField(Relatives)
    expiration_date = models.DateField()


  
