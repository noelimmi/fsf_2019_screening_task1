from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from usergroups.models import Team
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usergroups.forms import TeamCreationForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse


@login_required
def createteam(request):
    if request.method == 'POST':
        teamform = TeamCreationForm(request.POST, request.FILES)
        # Check if Data is Valid after submission
        if teamform.is_valid():
            team = teamform.save(commit=False)
            team.admin = request.user
            team.save()
            teamname = teamform.cleaned_data.get('name')
            messages.success(
                request, f'Team {teamname} has been created!')
            return redirect('listteam')
    else:
        teamform = TeamCreationForm()
    return render(request, 'usergroups/team_form.html', {'form': teamform})


@login_required
def change_teammember(request, userid, teamid, operation):
    user = get_object_or_404(User, pk=userid)
    team = get_object_or_404(Team, pk=teamid)
    if operation == 'add':
        team.member.add(user)
        messages.info(
            request, f'{user.username} has been added to your team!')
        return redirect('team-manager', pk=team.id)
    elif operation == 'remove':
        team.member.remove(user)
        messages.info(
            request, f'{user.username} has been removed from your team!')
        return redirect('team-manager', pk=team.id)
    else:
        messages.warning(
            request, f'{request.user.username} Please specify an action to perform!')
        return redirect('team-manager', pk=team.id)


@login_required
def list_team(request):
    context = {
        'yourteams': Team.objects.filter(admin=request.user),
        'enrolledteams': Team.objects.filter(member=request.user)
    }

    return render(request, 'usergroups/listteam.html', context)


class TeamDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        team = self.get_object()
        tmem = team.member.all()
        c_a = users.exclude(id__in=tmem.values_list('id', flat=True))
        non_member = c_a.exclude(id=self.request.user.id)
        context['nonmem'] = non_member
        return context

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.admin:
            return True
        return False


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    fields = ['name', 'description', 'teamicon']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        team = self.get_object()
        return reverse('team-manager', kwargs={'pk': team.id})

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.admin:
            return True
        return False


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    success_url = '/listteam/'

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.admin:
            return True
        return False
