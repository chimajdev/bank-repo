from django.contrib.auth import forms
from django.utils import timezone


class User(forms.User, forms.PermissionsMixin):
    
    def __str__(self):
        return self.username
