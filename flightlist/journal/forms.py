from django.contrib.auth.models import User
from django import forms
from journal.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class JournalForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'date', 'content', 'image')
        widgets = {
            'date': DateInput(),
        }

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)