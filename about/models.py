from django.db import models

class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    introduction = models.TextField(verbose_name="Вступление")
    history = models.TextField(verbose_name="История компании")
    mission = models.TextField(verbose_name="Миссия")
    meta_title = models.CharField(max_length=200, blank=True, verbose_name="Мета-заголовок")
    meta_description = models.TextField(blank=True, verbose_name="Мета-описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница О нас"
        verbose_name_plural = "Страница О нас"

class Value(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='values', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Название ценности")
    description = models.TextField(verbose_name="Описание ценности")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ценность"
        verbose_name_plural = "Ценности"

class TeamMember(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='team_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Имя")
    role = models.CharField(max_length=100, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='team_photos/', blank=True, verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

class Achievement(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='achievements', on_delete=models.CASCADE)
    number = models.CharField(max_length=50, verbose_name="Число (например, 150+)")
    description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return f"{self.number} - {self.description}"

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"

class Testimonial(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='testimonials', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    text = models.TextField(verbose_name="Текст отзыва")
    photo = models.ImageField(upload_to='testimonials/', blank=True, verbose_name="Фото клиента")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class GalleryItem(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='gallery_items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/', blank=True, verbose_name="Фото")
    video_url = models.URLField(blank=True, verbose_name="Ссылка на видео")

    def __str__(self):
        return f"Элемент галереи для {self.about_page.title}"

    class Meta:
        verbose_name = "Элемент галереи"
        verbose_name_plural = "Элементы галереи"

class ContactInfo(models.Model):
    about_page = models.ForeignKey(AboutPage, related_name='contact_info', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter")
    whatsapp_url = models.URLField(blank=True, verbose_name="WhatsApp")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")

    def __str__(self):
        return f"Контакты для {self.about_page.title}"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"