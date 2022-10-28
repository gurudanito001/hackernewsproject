import requests
import os
filepath = os.path.realpath(__file__)
dirname = os.path.dirname(filepath)
os.chdir(dirname)
from .serializers import StorySerializer


def save_story(storyData):
  serializer = StorySerializer(data=storyData)
  if serializer.is_valid():
    serializer.save() 

def initDb():
  allStories = requests.get("https://hacker-news.firebaseio.com/v0/showstories.json")
  allStoriesJson = allStories.json()
  firstStory = allStoriesJson[0]
  firstStoryDetails = requests.get("https://hacker-news.firebaseio.com/v0/item/" + str(firstStory) +  ".json")
  print(firstStoryDetails.json())
  save_story(firstStoryDetails.json())


initDb()