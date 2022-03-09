from rest_framework import serializers

from .models import IpModel

class IpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IpModel

        fields = (
            'id',
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
        