from django import forms
from .models import Team


class TeamCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Team name here...'
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Team description...'
        }
    ))

    class Meta:
        model = Team
        fields = ['name', 'description', 'teamicon']
