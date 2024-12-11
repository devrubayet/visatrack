from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Information)
admin.site.register(CheckStatus)
@admin.register(Slider)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'created_at')
    list_filter = ('is_active',)