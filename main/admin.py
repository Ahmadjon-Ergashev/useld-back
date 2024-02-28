from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Banner, Responsibility, GettingStarter, Platform
# Register your models here.

class BannerAdmin(TranslatableAdmin):
    list_display = ['title', 'body']
    url_field = ['title']


class GettingStarterAdmin(TranslatableAdmin):
    list_display = ['body']
    url_field = ['body']


class ResponsibilityAdmin(TranslatableAdmin):
    list_display = ['title', 'body']
    url_field = ['title']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
    url_field = ['title']


admin.site.register(Banner, BannerAdmin)
admin.site.register(Responsibility, ResponsibilityAdmin)
admin.site.register(GettingStarter, GettingStarterAdmin)
admin.site.register(Platform, PlatformAdmin)

