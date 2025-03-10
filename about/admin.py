from django.contrib import admin
from .models import AboutPage, Value, TeamMember, Achievement, Testimonial, GalleryItem, ContactInfo

class ValueInline(admin.TabularInline):
    model = Value
    extra = 1

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1

class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1

class GalleryItemInline(admin.TabularInline):
    model = GalleryItem
    extra = 1

class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [ValueInline, TeamMemberInline, AchievementInline, TestimonialInline, GalleryItemInline, ContactInfoInline]
    list_display = ('title',)