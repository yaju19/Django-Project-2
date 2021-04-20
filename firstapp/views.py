from django.shortcuts import render, HttpResponse
from firstapp.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'variable1': 'this is sent',
        'variable2': 'this is second variable'
    }
    # return HttpResponse("this is homepage")
    # messages.success(request, 'Profile details updated.')
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("this is about")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("this is services page")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, password=password).save()
        messages.success(request, 'Profile details have been saved.')
    return render(request, 'contact.html')
