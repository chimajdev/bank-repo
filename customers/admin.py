from django.contrib import admin
from .models import Account, Transaction

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number','owner','account_balance','date_created',)
    search_fields = ('account_number','owner',)
    list_filter = ('date_created',)
    # fields = ('owner','account_balance','account_type','last_deposit',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('owner','from_account','to_account','date_created',)
    search_fields = ('owner','from_account','to_account',)
    list_filter = ('date_created',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)