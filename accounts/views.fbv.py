from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            #user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('customers:dashboard')
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    username = request.POST['email']
    password = request.POST['password1']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    logout(request)





# CBV
# from django.contrib.auth import login, logout
# from django.urls import reverse_lazy
# from django.views.generic import CreateView

# from . import forms

# class SignUp(CreateView):
#     form_class = forms.SignUpForm
#     template_name = "accounts/signup.html"
