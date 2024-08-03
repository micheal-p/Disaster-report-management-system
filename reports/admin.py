from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ['disaster_type', 'location', 'description', 'date_reported', 'display_image', 'is_legitimate']

    def display_image(self, obj):
        return obj.image.url if obj.image else None

    display_image.short_description = 'Image'
    display_image.allow_tags = True

admin.site.register(Report, ReportAdmin)
