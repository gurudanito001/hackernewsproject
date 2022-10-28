from apscheduler.schedulers.background import BackgroundScheduler
from .views import fetchLatestStories

def printSomething():
  print("weeee")


def sheduleFetchStories():
  scheduler = BackgroundScheduler()
  scheduler.add_job(printSomething, "interval", seconds=5)
  scheduler.start()