from django.db import models

# Create your models here.
#
# class BaseModel(models.Model):
#     def to_json(self,queryset):
#         import json
#         res = json.dumps(list(data.values()))
#         return res
#     class Meta:
#         abstract = True

class Team(models.Model):
    tname = models.CharField(max_length=20)

    def __str__(self):
        return  self.tname

    class Meta:
        db_table = 'team'

class Student(models.Model):
    sname = models.CharField(max_length=30)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
    class Meta:
        db_table = 'student'
