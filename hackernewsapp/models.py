from email.policy import default
from enum import unique
from django.db import models


class Base(models.Model):
  id = models.IntegerField(primary_key=True, unique=True)
  deleted = models.BooleanField(default=False)
  type = models.CharField(max_length=20, default="")
  by = models.CharField(max_length=200, default="")
  time = models.IntegerField(null=True, default=None)
  dead = models.BooleanField(default=False)
  kids = models.JSONField()

class Job(Base):
  text = models.CharField(max_length=2000, default="")
  url = models.CharField(max_length=200, default="")
  title = models.CharField(max_length=2000, default="")

  def __str__(self):
    return self.title 

class Story(Base):
  descendants = models.IntegerField(default=0)
  score = models.IntegerField( default=0)
  title = models.CharField(max_length=2000, default="")
  url = models.CharField(max_length=200, default="")

  def __str__(self):
    return self.title 

class Comment(Base):
  parent = models.IntegerField(default=0)
  text = models.CharField(max_length=2000, default="")

class Poll(Base):
  parts = models.JSONField()
  descendants = models.IntegerField(default=0)
  score = models.IntegerField(default=0)
  title = models.CharField(max_length=2000, default="")
  text = models.CharField(max_length=2000, default="")

class PollOption(Base):
  parent = models.IntegerField(default=0)
  score = models.IntegerField(default=0)
      
    

  
