from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    # context = {
    #     'tasks': Task.objects.all()
    # }
    # only tasks of tht authenticated user
    context = {
        'tasks': request.user.tasks.all()
    }
    # to save owner when he create task
    return render(request, 'tasks/taskslist.html', context)
