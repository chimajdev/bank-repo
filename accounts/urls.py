from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url("login/$", views.Login.as_view(), name='login'),
    url("logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url("signup/$", views.signup, name="signup"),
    url("change-password/$", views.change_password, name="change_password"),
]
