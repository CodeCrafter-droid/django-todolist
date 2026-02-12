from django.contrib import admin
from .models import *
from django.urls import reverse
# Register your models here.

admin.site.register(taskdata)

admin.site.site_url = "/home"