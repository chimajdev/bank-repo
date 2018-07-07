from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from .forms import Transaction
from . import forms


@login_required(login_url='../../accounts/login/')
def dashboard(request):
    return render(request, template_name="customers/dashboard.html")

@login_required(login_url='../../accounts/login/')
def history(request):
    transaction = Transaction.objects.filter(owner=request.user)#.order_by(date_created)
    return render(request, "customers/transactions.html", {'transaction': transaction})


@login_required(login_url='../../accounts/login/')
def send(request):
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            trans =  form.save()
            return HttpResponseRedirect(reverse_lazy('customers:history'))
    else:
        form = forms.TransactionForm()
        return render(request, "customers/send_money.html", {'form': form})
