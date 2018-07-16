from django.utils import timezone
import decimal
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from .forms import Transaction
from . import forms
from accounts.forms import ProfileForm
from .models import Account


@login_required(login_url='../../accounts/login/')
def dashboard(request):
    account = Account.objects.get(owner=request.user)
    return render(request, "customers/dashboard.html", {'account': account})

@login_required(login_url='../../accounts/login/')
def history(request):
    transaction = Transaction.objects.filter(owner=request.user)#.order_by(date_created)
    return render(request, "customers/transactions.html", {'transaction': transaction})


@login_required(login_url='../../accounts/login/')
def send(request):
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            sender = Account.objects.get(account_number=request.POST.get('from_account'))
            if sender.account_balance > decimal.Decimal(request.POST.get('amount')):

                trans =  form.save()
                trans.owner = request.user
                trans.save()
                
                # debit the sender account
                sender.account_balance -= decimal.Decimal(request.POST.get('amount'))
                sender.save()

                #credit the receiver account
                receiver = Account.objects.get(account_number=request.POST.get('to_account'))
                receiver.account_balance += decimal.Decimal(request.POST.get('amount'))
                receiver.save()

                return HttpResponseRedirect(reverse_lazy('customers:history'))
            # else:
            #     return 
    else:
        form = forms.TransactionForm()
        return render(request, "customers/send_money.html", {'form': form})



@login_required(login_url='../../accounts/login/')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('customers:profile'))
    else:
        # form = ProfileForm()
        return render(request, "customers/profile.html")