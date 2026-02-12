from django.contrib import admin
from .models import *
# Register your models here.

class TaskDataAdmin(admin.ModelAdmin):
    list_display = ('task','user','created_at','updated_at','user_is_superuser')
    def user_is_superuser(self, obj):
        return obj.user.is_superuser

    user_is_superuser.boolean = True 
    user_is_superuser.short_description = "Is Superuser"
    
admin.site.register(taskdata, TaskDataAdmin)

admin.site.site_url = "/home"