from re import T
from django.db import models


class IpModel(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7)
    country = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=4)
    region = models.CharField(max_length=50, blank=True)
    regionName = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    zip = models.DecimalField(max_digits=100, decimal_places=10,null=True)
    lat = models.DecimalField(max_digits=100, decimal_places=10,null=False)
    lon = models.DecimalField(max_digits=100, decimal_places=10,null=False)
    timezone = models.CharField(max_length=50)
    isp = models.CharField(max_length=250)
    org = models.CharField(max_length=250, blank=True)
    _as = models.CharField(max_length=250, blank=True)
    query = models.CharField(max_length=15)
    class Meta:
      verbose_name = 'Ip'
      verbose_name_plural = 'Ips'
      ordering = ['id']

    def __str__(self) -> str:
      self.query

