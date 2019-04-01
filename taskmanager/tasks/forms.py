from django import forms
from .models import Task


class TeamTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'desc', 'assignee', 'status')

    def __init__(self, team, *args, **kwargs):
        super(TeamTaskForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].queryset = team.member.all()


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content = forms.CharField(label='', widget=forms.Textarea)
