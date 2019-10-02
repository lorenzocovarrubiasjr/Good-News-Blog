from django.http import HttpResponse
from django.shortcuts import render 
from .forms import ContactForm

def home_page(request):
    return render(request, "hello_world.html")

def home(request):
    return render(request, "home.html")

def contact(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"form": form}
    return render(request, 'contact.html', context)