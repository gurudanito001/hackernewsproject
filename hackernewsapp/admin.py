from django.contrib import admin
from .models import Job, Story, Comment, Poll, PollOption

admin.site.register([Job, Story, Comment, Poll, PollOption])