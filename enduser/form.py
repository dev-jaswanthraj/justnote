from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, forms
from django.forms import ModelForm
from django.forms import widgets
from .models import (
    note, 
    todo
)
class create(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class note_form(ModelForm):
    class Meta:
        model = note
        fields = ['title', 'content']

        widgets = {
            'title':forms.TextInput(attrs={'class':'btn btn-outline-warning my-2 my-sm-0', 'name':'title'}),
            'content':forms.Textarea(attrs={'class':'edittext btn-outline-warning my-2 my-sm-0', 'rows':'15', 'name':'content', 'style':"width: 100%; max-width: 100%; min-width: 100% 354152; height: 600px; resize: vertical;"})
        }
        