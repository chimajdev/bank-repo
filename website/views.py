from django.shortcuts import render, redirect

from .forms import ContactUsForm

# from django.shortcuts import render_to_response
# from django.template import RequestContext

def home(request):
    title = 'home'
    return render(request, "website/home.html" , {'title':home})

def about(request):
    title = 'about'
    return render(request, "website/about.html", {'title':about})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            form.save()
            # this_form.save()
            return redirect('website:home')
	# return render_to_response('website/contact.html', {'form':form}, RequestContext(request))
    return render(request, "website/contact.html", {'title':contact})

def gallery(request):
    title = 'gallery'
    return render(request, "website/gallery.html", {'title':gallery})

def services(request):
    title = 'services'
    return render(request, "website/services.html", {'title':services})
