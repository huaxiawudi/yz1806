from django.db import models

# Create your models here.
class Team(models.Model):
    tname = models.CharField(max_length=20)

    def __str__(self):
        return self.tname
    class Meta:
        db_table = 'team'

class Group1(models.Model):
    gname = models.CharField(max_length=20)
    team = models.ForeignKey(Team,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.gname
    class Meta:
        db_table = 'group1'


class Project(models.Model):
    pname = models.CharField(max_length=30)
    group1 = models.ManyToManyField(Group1)

    def __str__(self):
        return self.pname
    class Meta:
        db_table = 'project'