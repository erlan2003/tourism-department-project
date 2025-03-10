from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('tours/', include('tours.urls', namespace='tours')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('services/', include('services.urls', namespace='services')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)