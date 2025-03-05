from django.shortcuts import render

# Create your views here.

def open_contact(request):
    return render(request, 'contact.html')