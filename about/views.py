from django.shortcuts import render

# Create your views here.
def open_about(request):
    return render(request, 'about.html')