from django import forms
from .models import Team


class TeamCreationForm(forms.ModelForm):
    teamicon = forms.ImageField(label='Group Icon', required=False)

    class Meta:
        model = Team
        fields = ['name', 'description', 'teamicon']
