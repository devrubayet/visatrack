from django.contrib import admin
from .models import *
from django import forms
# Register your models here.


@admin.register(CheckStatus)
class CheckStatusAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'visa_name', 'visa_status', 'applicant_name', 'submission_date')


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 3  # Display 3 empty fields by default for adding social links
    max_num =3
    
    fields = ['platform_name', 'url']  # Show platform_name first, then url
    readonly_fields = ['platform_name']  # Make 'platform_name' read-only

class InformationAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    list_display = ('sitename', 'site_slogan', 'email', 'phone',  'logo', 'office_address', 'office_email', 'office_phone')
    
    def has_add_permission(self, request):
        return False  # Disable adding new record
    
    class Media:
        js = ('js/hide_add_another.js',)

admin.site.register(Information, InformationAdmin)



@admin.register(Slider)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'created_at')
    list_filter = ('is_active',)


class VisaImageInline(admin.TabularInline):
    model = VisaSilderImage
    extra = 3  # This will display 3 empty image fields by default for adding images.

class VisaListAdmin(admin.ModelAdmin):
    inlines = [VisaImageInline]  # Show VisaImage inline in the VisaList admin page

admin.site.register(VisaList, VisaListAdmin)


class PackageImageInline(admin.TabularInline):
    model = PackageSilderImage
    extra = 3  # This will display 3 empty image fields by default for adding images.

class PackageListAdmin(admin.ModelAdmin):
    inlines = [PackageImageInline]  # Show VisaImage inline in the VisaList admin page

admin.site.register(PackageList, PackageListAdmin)
