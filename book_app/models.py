from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.models import UserManager

class Books(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    publish_year = models.CharField(max_length = 100)
    edition = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title

        

class Member(AbstractUser):
    name = models.CharField(max_length = 50,unique=True)
    address = models.CharField(max_length = 50)
    phone_number =  models.CharField(max_length = 12)
   

    def __str__(self):
        return self.name


class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='member')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    expiration_date = models.DateField()

    @property
    def expired(self):
        return self.expiration_date < datetime.now().date()
