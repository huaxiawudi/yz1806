from django.db import models

# Create your models here.
# 自定义的model类必须继承子models.Model
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
