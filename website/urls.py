from django.urls import path

from .import views

app_name = 'website'

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('gallery', views.gallery, name='gallery')
]