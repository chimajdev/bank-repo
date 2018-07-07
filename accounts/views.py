from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView, FormView
# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from . import forms
from .forms import User

def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            #user.save()

            # manually set the user's password
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()

            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('customers:dashboard'))
    else:
        form = forms.SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})



class Login(LoginView):
    form_class = forms.LoginForm
    success_url = reverse_lazy("customers:dashboard")
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                )
            if user is not None:
                # if user.is_active:
                login(request, user)
                return HttpResponseRedirect(self.success_url)
                # else:
                #     return HttpResponse('User is not active') # TEMP
            else:
                return HttpResponse('User does not exist') # TEMP
        else:
            return render(request, 'accounts/login.html', {'form': forms.LoginForm})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('password1')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             form = forms.LoginForm()
#             return render(request, 'accounts/login.html', {'form': form})
#     else:
#         return render(request, 'accounts/login.html', {'form': forms.LoginForm()})

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("accounts:login"))



def change_password(request):
    form = forms.PasswordForm(request.POST)
    if request.method == 'POST':
        form = forms.PasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email=request.user.email)
            new_password = request.POST.get('password1')
            user.set_password(new_password)
            user.save()
            # log the user in again
            login(request, user)
            # update user sessions
            update_session_auth_hash(request, request.user)
            return HttpResponseRedirect(reverse_lazy("customers:dashboard"))
    else:
        return render(request ,"accounts/change-password.html", {'form':form})