from django.shortcuts import render
from main.models import TourType
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import logging

def open_main(request):
    tour_types = TourType.objects.all()
    return render(request, 'main.html', {'tour_types': tour_types})


def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            send_mail(
                'Тема сообщения',
                message,
                'kudajberdieverlan7@gmail.com',  # Отправитель
                ['erlankudajberdiev2@gmail.com'],  # Получатель
                fail_silently=False,
            )
            return JsonResponse({"message": "Сообщение отправлено!"})
        except Exception as e:
            return JsonResponse({"message": f"Ошибка при отправке: {str(e)}"}, status=500)