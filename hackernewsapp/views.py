from .models import Story, Job, Comment, Poll, PollOption
from .serializers import StorySerializer, JobSerializer, CommentSerializer, PollSerializer, PollOptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

""" STORY VIEWS """

""" def save_story(storyData):
  serializer = StorySerializer(data=storyData)
  if serializer.is_valid():
      serializer.save()
 """

def fetchLatestStories(request, format=None):
  try:
    topStories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    allStoriesJson = topStories.json()

    for storyId in allStoriesJson:
      story = Story.objects.get(pk=storyId)
      if story:
        continue
      storyDetails = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(storyId) +  ".json")
    
      serializer = StorySerializer(data=storyDetails.json())
      if serializer.is_valid():
        serializer.save()
        
    return print("all done")
  except:
    return 

  

@api_view(['GET', 'POST'])
def story_list(request, format=None):

  if request.method == 'GET':
    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = StorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def story_details(request, id, format=None):

  try:
    story = Story.objects.get(pk=id)
  except Story.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if(request.method == 'GET'):
    serializer = StorySerializer(story)
    return Response(serializer.data)

  elif(request.method == 'PUT'):
    serializer = StorySerializer(story, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif(request.method == 'DELETE'):
    story.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


""" JOB VIEWS """
@api_view(['GET', 'POST'])
def job_list(request, format=None):

  if request.method == 'GET':
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def job_details(request, id, format=None):

  try:
    job = Job.objects.get(pk=id)
  except Job.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if(request.method == 'GET'):
    serializer = JobSerializer(job)
    return Response(serializer.data)

  elif(request.method == 'PUT'):
    serializer = JobSerializer(job, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif(request.method == 'DELETE'):
    job.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


""" COMMENT VIEWS """
@api_view(['GET', 'POST'])
def comment_list(request, format=None):

  if request.method == 'GET':
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_details(request, id, format=None):

  try:
    comment = Comment.objects.get(pk=id)
  except Comment.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if(request.method == 'GET'):
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

  elif(request.method == 'PUT'):
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif(request.method == 'DELETE'):
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


""" POLL VIEWS """
@api_view(['GET', 'POST'])
def poll_list(request, format=None):

  if request.method == 'GET':
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = PollSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def poll_details(request, id, format=None):

  try:
    poll = Poll.objects.get(pk=id)
  except Poll.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if(request.method == 'GET'):
    serializer = PollSerializer(poll)
    return Response(serializer.data)

  elif(request.method == 'PUT'):
    serializer = PollSerializer(poll, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif(request.method == 'DELETE'):
    poll.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



""" POLL OPTION VIEWS """

@api_view(['GET', 'POST'])
def pollOption_list(request, format=None):

  if request.method == 'GET':
    pollOptions = PollOption.objects.all()
    serializer = PollOptionSerializer(pollOptions, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = PollOptionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pollOption_details(request, id, format=None):

  try:
    pollOption = PollOption.objects.get(pk=id)
  except PollOption.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if(request.method == 'GET'):
    serializer = PollOptionSerializer(pollOption)
    return Response(serializer.data)

  elif(request.method == 'PUT'):
    serializer = PollOptionSerializer(pollOption, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif(request.method == 'DELETE'):
    pollOption.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)