from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    institution = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','institution','password1','password2')
