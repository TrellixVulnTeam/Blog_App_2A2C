from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


# This class is inharit from UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']