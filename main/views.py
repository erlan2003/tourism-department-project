from django.shortcuts import render
from main.models import TourType
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.encoding import smart_str

def open_main(request):
    tour_types = TourType.objects.all()
    return render(request, 'main.html', {'tour_types': tour_types})


def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            # Убедитесь, что сообщение правильно закодировано в UTF-8
            send_mail(
                'Ваш запрос принят',
                smart_str(f"Мы получили ваш запрос: '{message}'. Мы свяжемся с вами."),
                'kudajberdieverlan7@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({"message": "Ваш запрос принят! Мы свяжемся с вами."})
        except Exception as e:
            return JsonResponse({"message": f"Ошибка при отправке: {str(e)}"}, status=500)
