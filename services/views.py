from django.shortcuts import render

def services_page(request):
    services = [
        {'name': 'Машина с гидом', 'description': 'Аренда автомобиля с русскоязычным гидом'},
        {'name': 'Индивидуальный гид', 'description': 'Персональный гид для экскурсий'},
        {'name': 'Трансфер', 'description': 'Комфортабельный трансфер в любую точку'},
    ]
    return render(request, 'services/services.html', {'services': services})