from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from usergroups.models import Team
from django.contrib.auth.decorators import login_required


@login_required
def add_teammember(request, username, teamname):
    new_member = get_object_or_404(User, username=username)
    team = get_object_or_404(User, name=teamname)
    admin = request.user
    team.add_member(admin, new_member)
    return redirect(new_member.get_absolute_url())


@login_required
def remove_teammember(request, username, teamname):
    member = get_object_or_404(User, username=username)
    team = get_object_or_404(Team, name=teamname)
    admin = request.user
    team.remove_member(admin, new_member)
    return redirect(member.get_absolute_url())


@login_required
def list_members(request):
    team, created = Team.objects.get_or_create(admin=request.user)
    members = [member for member in team.member.all() if member !=
               request.user]
    return render(request, 'usergroups/listmembers.html', {"members": members})
