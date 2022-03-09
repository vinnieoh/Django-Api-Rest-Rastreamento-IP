from django.urls import path

from .views import IpAPIView, IpsAPIView

urlpatterns = [
    path('ip/',IpAPIView.as_view(), name='ip'),
    path('ips/',IpsAPIView.as_view(), name='ips'),
]
