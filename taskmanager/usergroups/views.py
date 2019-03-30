from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from usergroups.models import Team
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usergroups.forms import TeamCreationForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def createteam(request):
    if request.method == 'POST':
        teamform = TeamCreationForm(request.POST)
        # Check if Data is Valid after submission
        if teamform.is_valid():
            team = teamform.save(commit=False)
            team.admin = request.user
            team.save()
            teamname = teamform.cleaned_data.get('name')
            messages.success(
                request, f'Team {teamname} has been created!')
            return redirect('create-team')
    else:
        teamform = TeamCreationForm()
    return render(request, 'usergroups/teamcreate.html', {'teamform': teamform})


@login_required
def change_teammember(request, username, teamname, operation):
    user = get_object_or_404(User, username=username)
    team = get_object_or_404(User, name=teamname)
    if operation == 'add':
        team.member.add(user)
        messages.success(
            request, f'{user.username} has been added to your team!')
        return render(request, 'usergroups/team_detail.html', {'object': team})
    elif operation == 'remove':
        team.member.remove(user)
        messages.success(
            request, f'{user.username} has been removed from your team!')
        return render(request, 'usergroups/team_detail.html', {'object': team})
    else:
        messages.warning(
            request, f'{request.user.username} Please specify an action to perform!')
        return redirect('team-manager')


@login_required
def list_team(request):
    context = {
        'yourteams': Team.objects.filter(admin=request.user),
        'enrolledteams': Team.objects.filter(member=request.user)
    }

    return render(request, 'usergroups/listteam.html', context)


@login_required
def list_available_user(request, teamid):
    team = get_object_or_404(Team, pk=teamid)
    users = User.objects.all()
    tmem = team.member.all()
    c_a = users.exclude(id__in=tmem.values_list('id', flat=True))
    non_member = c_a.exclude(id=request.user.id)
    return render(request, 'usergroups/listnonteammem.html', {'nonmem': non_member})


class TeamDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Team

    def test_func(self):
        team = self.get_object()
        if self.request.user == team.admin:
            return True
        return False
