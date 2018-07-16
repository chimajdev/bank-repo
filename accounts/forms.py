from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.views.generic import FormView
from .models import User, Profile


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={ 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    
    
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)


class PasswordForm(forms.Form):
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control border-input'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control border-input'}))
    # bio = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':'5','class':'form-control border-input','placeholder': 'Your Biography'}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Address','class':'form-control border-input'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control border-input'}))
    country = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Country','class':'form-control border-input'}))
    zip_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Zip Code','class':'form-control border-input'}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','address', 'city','country','zip_code',)