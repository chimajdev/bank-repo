from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    from_account = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'From account'}))
    to_account = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'To account'}))
    amount = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Amount to send'}))

    class Meta:
        model = Transaction
        fields = ('from_account', 'to_account', 'amount',)