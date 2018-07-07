from django.shortcuts import render

def home(request):
    title = 'home'
    return render(request, "website/home.html" , {'title':home})

def about(request):
    title = 'about'
    return render(request, "website/about.html", {'title':about})

def contact(request):
    title = 'contact'
    return render(request, "website/contact.html", {'title':contact})

def gallery(request):
    title = 'gallery'
    return render(request, "website/gallery.html", {'title':gallery})

def services(request):
    title = 'services'
    return render(request, "website/services.html", {'title':services})
