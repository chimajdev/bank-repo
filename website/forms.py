from django import forms
from .models import Contact


class ContactUsForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput())
    # email = forms.CharField(widget=forms.TextInput())
    # message = forms.CharField(widget=forms.Textarea())
	
    class Meta:
        model = Contact
        fields = ('name', 'email','message')