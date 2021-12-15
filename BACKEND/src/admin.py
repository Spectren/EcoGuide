from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([RecycleType, Project, ProjectMark, WallPost, Advert, PickPoint, Event, EventMark])