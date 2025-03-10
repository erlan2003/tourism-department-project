from django.contrib import admin
from .models import ContactInfo, ContactMessage

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone', 'whatsapp_link', 'instagram_link')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')  # Только для чтения