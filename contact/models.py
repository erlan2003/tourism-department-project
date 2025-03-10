from django.db import models

class ContactInfo(models.Model):
    address = models.TextField(verbose_name="Адрес", blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон (WhatsApp)", blank=True)
    whatsapp_link = models.URLField(verbose_name="Ссылка на WhatsApp", blank=True)
    instagram_link = models.URLField(verbose_name="Ссылка на Instagram", blank=True)

    def __str__(self):
        return f"Контактная информация"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Сообщение от {self.name}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"