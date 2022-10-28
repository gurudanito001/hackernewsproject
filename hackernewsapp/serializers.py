from rest_framework import serializers
from .models import Story, Job, Comment, Poll, PollOption

baseFields = ['id', 'deleted', 'type', 'by', 'time', 'dead', 'kids']
class StorySerializer(serializers.ModelSerializer):
  class Meta: 
    model = Story
    fields = [*baseFields, 'descendants', 'score', 'title', 'url']

class JobSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Job
    fields = [*baseFields, 'text',  'url', 'title']

class CommentSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Comment
    fields = [*baseFields, 'parent', 'text']

class PollSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Poll
    fields = [*baseFields, 'parts', 'descendants', 'score', 'title', 'text']

class PollOptionSerializer(serializers.ModelSerializer):
  class Meta: 
    model = PollOption
    fields = [*baseFields, 'parent', 'score']