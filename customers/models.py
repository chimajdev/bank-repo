from django.utils import timezone

from django.db import models
from django import forms
from accounts.models import User

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SA' , 'Savings Account' ),
        ('CA' , 'Current Account' ),
        ('JA' , 'Joint Account' ),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', verbose_name='The related user')
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES)
    account_number = models.CharField(max_length=13, unique=True)
    account_balance = models.DecimalField(max_digits=18, decimal_places=2)
    last_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=3, decimal_places=0)
    date_created = models.DateField()

    def __str__(self):
        return self.account_number

    # def save(self, *args, **kwargs):
    #     do_something()
    #     super(Account, self).save(*args, **kwargs) # Call the "real" save() method.


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    from_account = models.CharField(max_length=13)
    to_account = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField()

    def __str__(self):
        return str(self.amount)