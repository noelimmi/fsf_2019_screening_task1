from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from usergroups.models import Team
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TeamTaskForm
from django.http import HttpResponseForbidden


class TaskListView(LoginRequiredMixin, ListView):
    context_object_name = 'tasks'
    template_name = 'tasks/taskslist.html'
    model = Task
    ordering = ['-created_at']

    def get_queryset(self):
        """
        Since user can be admin for many teams,so on his personal dashboard only should
        be populated by tasks made by him without the one from any of his team
        """
        return self.request.user.tasks.filter(assignee=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'desc', 'status']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.owner:
            return True
        return False


class TeamTaskListView(LoginRequiredMixin, UserPassesTestMixin, ListView):

    context_object_name = 'tasks'
    template_name = 'tasks/taskslist.html'
    model = Task
    ordering = ['-created_at']

    def get_queryset(self):
        """
        Only Task associated with team should be shown
        """
        team = get_object_or_404(Team, pk=self.kwargs['teamid'])
        return team.teamtasks.all()

    def test_func(self):
        team = get_object_or_404(Team, pk=self.kwargs['teamid'])
        if self.request.user == team.admin or self.request.user.teammembers.filter(id=team.id).exists():
            return True
        return False


class TeamTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task

    def get_success_url(self):
        task = self.get_object()
        team = task.team
        return reverse('team-task-manager', kwargs={'teamid': team.id})

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.team.admin:
            return True
        return False


@login_required
def teamtaskcreate(request, teamid):
    if request.method == 'POST':
        team = get_object_or_404(Team, pk=teamid)
        form = TeamTaskForm(team, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team = team
            task.owner = team.admin
            task.save()
            return redirect('team-task-manager', teamid=team.id)
    else:
        team = get_object_or_404(Team, pk=teamid)
        form = TeamTaskForm(team)
        return render(request, 'tasks/task_form.html', {'form': form})
