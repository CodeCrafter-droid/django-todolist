from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import taskdata
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def publichome(request):
     
     return render(request,'publichome.html')

@never_cache
@login_required(login_url='signup_login')
def home(request):
    if request.user.is_authenticated:
        td = taskdata.objects.filter(user=request.user)
    else:
        td = taskdata.objects.none() 

    return render(request,'home.html',{'td':td})


def addtask(request):
        if request.method == "POST": 
         data = request.POST["data"]
        if data:
            taskdata.objects.create(user=request.user,task=data)
        else:
            messages.error(request, "Task cannot be empty")
            
        return redirect("home")


def markdone(request, pk):
        task = get_object_or_404(taskdata, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('home') 


def undotask(request, pk):
        task = get_object_or_404(taskdata, pk=pk)
        task.is_completed = False
        task.save()
        return redirect('home') 
     

def deletetask(request, pk):
        task = get_object_or_404(taskdata, pk=pk)
        task.delete()
        return redirect('home') 


def edittask(request, pk):
    task = get_object_or_404(taskdata, pk=pk)

    if request.method == "POST":
        data = request.POST.get('task', '').strip()
        if data:
            task.task = data
            task.save()
            return redirect('home')

    # GET request → open edit page
    return render(request, 'edittask.html', {
        'td': task
    })





