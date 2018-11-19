from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'animal'

class Dog(Animal):
    age = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.age)

    class Meta:
        db_table = 'dog'

# 抽象父类
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)

    class Meta:
        abstract = True   #父类是抽象的，不生成表

class Child(Person):
    sex = models.CharField(max_length=2)
