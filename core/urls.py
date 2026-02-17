from django.urls import path
from . import views

urlpatterns = [
    path("",views.publichome,name='publichome'),
    path("home",views.home,name='home'),
    path("addtask",views.addtask,name="addtask"),
    path("mark_done/<int:pk>",views.markdone,name="mark_done"),
    path("delete_task/<int:pk>",views.deletetask,name="delete_task"),
    path("edit_task/<int:pk>",views.edittask,name="edit_task"),
    path("undo_task/<int:pk>",views.undotask,name="undo_task"),
    # path("api/demo/",views.demo_api,name="demo_api"),
]


