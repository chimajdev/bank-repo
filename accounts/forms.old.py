from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class SignupForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Username'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={ 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password Again'}))

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["username"].label = ""

class AuthForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    