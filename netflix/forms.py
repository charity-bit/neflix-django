from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.forms import AuthenticationForm


from django import forms

from .models import User

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")


class GetStartedForm(forms.Form):
    email = forms.EmailField()
  
        