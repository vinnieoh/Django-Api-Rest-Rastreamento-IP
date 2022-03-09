from django.contrib import admin

from .models import IpModel


@admin.register(IpModel)
class IpAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'country',
        'countryCode',
        'region',
        'regionName',
        'city',
        'zip', 
        'lat', 
        'lon', 
        'timezone', 
        'isp', 
        'org', 
        '_as', 
        'query',
    )