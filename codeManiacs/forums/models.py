from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Forum(models.Model):
    question = models.CharField(max_length = 200)
    description  = models.CharField(max_length = 1000, default = "")
    tags = models.CharField(max_length = 100, default = "")
    author = models.CharField(max_length = 200)
    dateCreated = models.DateTimeField(default = datetime.now)
    upVote = models.IntegerField(default = 0)
    downVote = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    question = models.OneToOneField(Forum)
    answer = models.CharField(max_length = 5000)
    author = models.CharField(max_length = 200)
    dateAnswered = models.DateTimeField(default = datetime.now)
    upVote = models.IntegerField(default = 0)
    downVote = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.answer