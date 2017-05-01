from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProblemSet(models.Model):
    #pid = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    difficulty = models.CharField(max_length = 10)
    submissions = models.IntegerField(default = 0)
    accuracy = models.FloatField(default = 0.0)
    tags = models.CharField(max_length = 200,default="")

    def __unicode__(self):
        return self.title