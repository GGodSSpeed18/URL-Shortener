from django import forms
from .models import URLdata
from django.forms import ModelForm

class URL_postform(ModelForm):
    class Meta:
        model = URLdata
        fields = ['name','long_url']
        widgets={
            'name': forms.TextInput(
                attrs={'placeholder': 'Link to...'}
            ),
            'long_url': forms.TextInput(
                attrs={'placeholder':'URL...'}
            ),
        }
