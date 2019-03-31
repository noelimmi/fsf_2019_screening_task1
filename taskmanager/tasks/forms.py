from django import forms
from .models import Task


class TeamTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'desc', 'assignee', 'status')

    def __init__(self, team, *args, **kwargs):
        super(TeamTaskForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].queryset = team.member.all()
