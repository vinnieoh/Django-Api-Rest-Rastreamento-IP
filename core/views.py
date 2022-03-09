from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .utils import ip_search
from .serializers import IpSerializer
from .models import IpModel


class IpAPIView(APIView):

   
    def post(self, request):
        data = ip_search(request.data)

        serializer = IpSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IpsAPIView(generics.ListAPIView):
    queryset = IpModel.objects.all()
    serializer_class = IpSerializer
        

