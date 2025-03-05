from django.shortcuts import render

# Create your views here.
def open_tours(request):
    return render(request, 'tours.html')