from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfo, ContactMessage
from main.models import TourType
def contact(request):
    contact_info = ContactInfo.objects.first()
    tour_types = TourType.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:  # Простая проверка на заполненность
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Ваше сообщение успешно отправлено!")
        else:
            messages.error(request, "Ошибка: все поля должны быть заполнены!")
        return redirect('contact:contact')
    return render(request, 'contact/contact.html', {'contact_info': contact_info , 'tour_types': tour_types})

def submit_message(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:  # Простая проверка на заполненность
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Ваше сообщение успешно отправлено!")
        else:
            messages.error(request, "Ошибка: все поля должны быть заполнены!")
        return redirect('contact:contact')
    return redirect('contact:contact')