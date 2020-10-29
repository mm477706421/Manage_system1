from django.db import models
import datetime


# Create your models here.
class UserAgent(models.Model):
    username = models.CharField(max_length=16)
    passwd = models.CharField(max_length=16)
    reg_date_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    issuperuser = models.CharField(max_length=10,default="False")

    class Meta:
        ordering = ['reg_date_time']

class Event(models.Model):
    name = models.CharField(max_length=16)
    yuanxi = models.CharField(max_length=16)
    date = models.DateTimeField(default=datetime.datetime.now())
    detail = models.CharField(max_length=1000)

    class Meta:
        ordering = ['date']